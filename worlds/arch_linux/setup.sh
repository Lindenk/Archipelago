#!/usr/bin/env bash
set -e

# Make sure the user is running an Arch Linux iso, on the off chance
# they accidentally run this on their host system
if [ $(cat /etc/hostname) != "archiso" ]; then
  echo "Non Arch Linux ISO detected! Aborting..."
  exit 1
fi

function general_setup() {
  # increase space on ramdisk
  mount -o remount,size=8G /run/archiso/cowspace

  # disable debug aur builds
  sed -i -e '/^OPTIONS/s/ debug/ !debug/' -e '/^OPTIONS/s/ lto/ !lto/' /etc/makepkg.conf
}

function setup_chroot() {
  # check if we've done this already
  if [ -d /ap ]; then
    umount -R /ap
    rm -rf /ap
  fi

  # Put our chroot in a tmpfs so we can mount an overlay
  mkdir /ap
  mount -t tmpfs tmpfs /ap

  mkdir /ap/base /ap/bin
  cd /ap/base
  mkdir boot dev etc home mnt opt proc root run srv sys tmp usr var
  mkdir usr/bin usr/etc usr/include usr/lib usr/local usr/share usr/src

  mount -o bind /boot boot
  mount -o bind /dev dev
  mount -o bind /etc etc
  mount -o bind /proc proc
  #mount -o bind /root root
  mount -o bind /run run
  mount -o bind /srv srv
  mount -o bind /sys sys
  mount -o bind /tmp tmp
  mount -o bind /var var

  mount -o bind /ap/bin usr/bin
  mount -o bind /usr/etc usr/etc
  mount -o bind /usr/include usr/include
  mount -o bind /usr/lib usr/lib
  mount -o bind /usr/local usr/local
  mount -o bind /usr/share usr/share
  mount -o bind /usr/src usr/src

  ln -s usr/bin bin
  ln -s usr/lib lib
  ln -s usr/lib lib64
  ln -s usr/bin sbin

  ln -s lib usr/lib64
  ln -s bin usr/sbin

  # bind mount initial tools
  cd /ap/bin
  for p in bash zsh ls grep uname; do
    touch $p
    mount -o bind /bin/$p $p
  done
}

function setup_zsh() {
  cd /ap/base/root
  mkdir .cache

  # remove the global zshrc so they don't mess with the chroot
  # prompt
  mv /etc/zsh/zshrc /root/.zshrc
  mv /etc/zsh/zprofile /root/.zprofile

  # Set our prompt
  echo 'PS1="apuser@apworld %1 #"' > /ap/base/root/.zshenv
}

function setup_archipelago_service() {
  # Create a python script to run the client
  echo '
import asyncio
import websockets
import json
import sys
import subprocess
import os
import argparse

async def run_command(cmd):
    pass # TODO: Find which progs to bind mount

async def connect_to_multiworld(uri, user, password):
    async with websockets.connect(uri) as websocket:
        # Send connect message
        await websocket.send(json.dumps({
            "cmd": "Connect",
            "game": "Arch Linux", 
            "name": user,
            "uuid": "archlinux_client",
            "version": "0.4.2",
            "password": password
        }))

        while True:
            try:
                msg = await websocket.recv()
                data = json.loads(msg)
                
                if data.get("cmd") == "ReceivedItems":
                    for item in data["items"]:
                        # Execute the received command
                        if "command" in item:
                            await run_command(item["command"])
                            
                elif data.get("cmd") == "RoomUpdate":
                    # Handle room updates
                    pass

            except websockets.exceptions.ConnectionClosed:
                print("Connection closed, attempting to reconnect...")
                break
            except Exception as e:
                print(f"Error: {e}")
                break

async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('uri', help='WebSocket URI to connect to')
    parser.add_argument('user', help='Username to connect with')
    parser.add_argument('password', help='Password for authentication')
    args = parser.parse_args()

    # Validate URI
    try:
        parsed_uri = urllib.parse.urlparse(args.uri)
        if parsed_uri.scheme not in ['ws', 'wss']:
            print("Error: URI must start with ws:// or wss://")
            sys.exit(1)
    except Exception as e:
        print(f"Invalid URI format: {e}")
        sys.exit(1)

    # Validate username is not empty
    if not args.user:
        print("Error: Username cannot be empty")
        sys.exit(1)

    while True:
        try:
            await connect_to_multiworld(args.uri, args.user, args.password)
        except:
            print("Connection failed, retrying in 30 seconds...")
            await asyncio.sleep(30)

if __name__ == "__main__":
    asyncio.run(main())


  " > /ap/archipelago-client.py

  # Create the service file
  echo "
  [Unit]
  Description=Archipelago ClientService
  After=network.target

  [Service]
  Type=simple
  ExecStart=/ap/archipelago-client.py
  ' > /etc/systemd/system/archipelago-client.service
}

general_setup
setup_chroot
setup_zsh
setup_archipelago_service

