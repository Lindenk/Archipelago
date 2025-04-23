from BaseClasses import ItemClassification as IC
from typing import List, NamedTuple, TypedDict, Dict, Set
  
item_base_id = 828973100

class PackageItemData(NamedTuple):
  classification: IC
  item_group: str = ""
  commands: List[str] = []

class PackageGroupItemData(NamedTuple):
  classification: IC
  item_group: str = ""
  packages: List[str] = []


packages = {
  "alsa-utils": PackageItemData(IC.filler, ["aconnect",
    "alsa-info.sh",
    "alsabat",
    "alsabat-test.sh", 
    "alsactl",
    "alsaloop",
    "alsamixer",
    "alsatplg",
    "alsaucm",
    "amidi",
    "amixer", 
    "aplay",
    "aplaymidi",
    "aplaymidi2",
    "arecord",
    "arecordmidi",
    "arecordmidi2",
    "aseqdump",
    "aseqnet",
    "aseqsend",
    "axfer",
    "iecset",
    "nhlt-dmic-info",
    "speaker-test"
  ]),

  # Arch Install Scripts
  "arch-install-scripts": PackageItemData(IC.progression, ["arch-chroot", "pacstrap"]),
  "genfstab": PackageItemData(IC.progression),

  "b43-fwcutter": PackageItemData(IC.filler),

  # Base
  "archlinux-keyring": PackageItemData(IC.progression, ["archlinux-keyring-wkd-sync"]),
  "bzip2": PackageItemData(IC.filler, ["bunzip2", "bzcat", "bzdiff", "bzgrep", "bzip2", "bzip2recover", "bzmore"]),
  # Checksum and hashing tools
  "coreutils-hashing": PackageItemData(IC.progression, [
    "b2sum", "cksum", "md5sum", "sha1sum", "sha224sum", 
    "sha256sum", "sha384sum", "sha512sum", "sum", "base32", "base64"
  ]),

  # Text processing tools
  "coreutils-text": PackageItemData(IC.progression, [
    "basename", "basenc", "cat", "comm", "cut", 
    "expand", "fmt", "fold", "head", "join", "nl", "od", "paste", 
    "pr", "ptx", "sort", "split", "tac", "tail", "tr", "tsort", 
    "unexpand", "uniq", "wc"
  ]),

  # File operations
  "coreutils-files": PackageItemData(IC.progression, [
    "cp", "csplit", "dd", "df", "dir", "dircolors", "dirname", "du", 
    "install", "link", "ln", "ls", "mkdir", "mkfifo", "mknod", "mktemp", 
    "mv", "pwd", "readlink", "realpath", "rm", "rmdir", "shred", "stat", 
    "sync", "touch", "truncate", "unlink", "vdir", "tee", "file", "find"
  ]),

  # File permissions
  "coreutils-permissions": PackageItemData(IC.progression, [
    "chcon", "chgrp", "chmod", "chown", "chroot"
  ]),

  # Process/system tools
  "coreutils-proc": PackageItemData(IC.progression, [
    "env", "expr", "hostid", "nice", "nohup", "nproc", "numfmt", 
    "printenv", "printf", "runcon", "seq", "sleep", "stdbuf", "stty", 
    "timeout", "tty", "uname", "xargs"
  ]),

  # User info tools
  "coreutils-user": PackageItemData(IC.progression, [
    "groups", "id", "logname", "users", "who", "whoami"
  ]),

  "coreutils-logic": PackageItemData(IC.filler, [
    "true", "false", "test"
  ]),

  # Other utilities
  "coreutils-other": PackageItemData(IC.filler, [
    "date", "echo", "factor", "pathchk", "pinky", "shuf", "yes"
  ]),

  "awk": PackageItemData(IC.useful, ["awk", "gawk", "gawkbug"]),
  "sed": PackageItemData(IC.useful),

  "base": PackageItemData(IC.filler),
  "bcachefs-tools": PackageItemData(IC.filler),
  "bind": PackageItemData(IC.filler),
  "bolt": PackageItemData(IC.filler),
  "brltty": PackageItemData(IC.filler),
  "broadcom-wl": PackageItemData(IC.filler),
  "btrfs-progs": PackageItemData(IC.filler),
  "clonezilla": PackageItemData(IC.filler),
  "cloud-init": PackageItemData(IC.filler),
  "cryptsetup": PackageItemData(IC.filler),
  "darkhttpd": PackageItemData(IC.filler),
  "ddrescue": PackageItemData(IC.filler),
  "dhcpcd": PackageItemData(IC.filler),
  "diffutils": PackageItemData(IC.filler),
  "dmidecode": PackageItemData(IC.filler),
  "dmraid": PackageItemData(IC.filler),
  "dnsmasq": PackageItemData(IC.filler),
  "dosfstools": PackageItemData(IC.filler),
  "e2fsprogs": PackageItemData(IC.filler),
  "edk2-shell": PackageItemData(IC.filler),
  "efibootmgr": PackageItemData(IC.filler),
  "espeakup": PackageItemData(IC.filler),
  "ethtool": PackageItemData(IC.filler),
  "exfatprogs": PackageItemData(IC.filler),
  "f2fs-tools": PackageItemData(IC.filler),
  "fatresize": PackageItemData(IC.filler),
  "foot-terminfo": PackageItemData(IC.filler),
  "fsarchiver": PackageItemData(IC.filler),
  "gpart": PackageItemData(IC.filler),
  "gpm": PackageItemData(IC.filler),
  "gptfdisk": PackageItemData(IC.filler),
  "grml-zsh-config": PackageItemData(IC.filler),
  "grub": PackageItemData(IC.filler),
  "hdparm": PackageItemData(IC.filler),
  "hyperv": PackageItemData(IC.filler),
  "irssi": PackageItemData(IC.filler),
  "iw": PackageItemData(IC.filler),
  "iwd": PackageItemData(IC.filler),
  "jfsutils": PackageItemData(IC.filler),
  "kitty-terminfo": PackageItemData(IC.filler),
  "ldns": PackageItemData(IC.filler),
  "less": PackageItemData(IC.filler),
  "lftp": PackageItemData(IC.filler),
  "libfido2": PackageItemData(IC.filler),
  "libusb-compat": PackageItemData(IC.filler),
  "linux-atm": PackageItemData(IC.filler),
  "livecd-sounds": PackageItemData(IC.filler),
  "lsscsi": PackageItemData(IC.filler),
  "lvm2": PackageItemData(IC.filler),
  "lynx": PackageItemData(IC.filler),
  "man-db": PackageItemData(IC.filler),
  "man-pages": PackageItemData(IC.filler),
  "mc": PackageItemData(IC.filler),
  "mdadm": PackageItemData(IC.filler),
  "memtest86+": PackageItemData(IC.filler),
  "memtest86+-efi": PackageItemData(IC.filler),
  "mkinitcpio": PackageItemData(IC.filler),
  "mkinitcpio-archiso": PackageItemData(IC.filler),
  "mkinitcpio-nfs-utils": PackageItemData(IC.filler),
  "modemmanager": PackageItemData(IC.filler),
  "mtools": PackageItemData(IC.filler),
  "nano": PackageItemData(IC.filler),
  "nbd": PackageItemData(IC.filler),
  "ndisc6": PackageItemData(IC.filler),
  "nfs-utils": PackageItemData(IC.filler),
  "nilfs-utils": PackageItemData(IC.filler),
  "nmap": PackageItemData(IC.filler),
  "ntfs-3g": PackageItemData(IC.filler),
  "nvme-cli": PackageItemData(IC.filler),
  "open-iscsi": PackageItemData(IC.filler),
  "open-vm-tools": PackageItemData(IC.filler),
  "openconnect": PackageItemData(IC.filler),
  "openpgp-card-tools": PackageItemData(IC.filler),
  "openssh": PackageItemData(IC.filler),
  "openvpn": PackageItemData(IC.filler),
  "partclone": PackageItemData(IC.filler),
  "parted": PackageItemData(IC.filler),
  "partimage": PackageItemData(IC.filler),
  "pcsclite": PackageItemData(IC.filler),
  "ppp": PackageItemData(IC.filler),
  "pptpclient": PackageItemData(IC.filler),
  "pv": PackageItemData(IC.filler),
  "qemu-guest-agent": PackageItemData(IC.filler),
  "refind": PackageItemData(IC.filler),
  "reflector": PackageItemData(IC.filler),
  "rp-pppoe": PackageItemData(IC.filler),
  "rsync": PackageItemData(IC.filler),
  "rxvt-unicode-terminfo": PackageItemData(IC.filler),
  "screen": PackageItemData(IC.filler),
  "sdparm": PackageItemData(IC.filler),
  "sequoia-sq": PackageItemData(IC.filler),
  "sg3_utils": PackageItemData(IC.filler),
  "smartmontools": PackageItemData(IC.filler),
  "sof-firmware": PackageItemData(IC.filler),
  "squashfs-tools": PackageItemData(IC.filler),
  "sudo": PackageItemData(IC.filler),
  "syslinux": PackageItemData(IC.filler),
  "systemd-resolvconf": PackageItemData(IC.filler),
  "tcpdump": PackageItemData(IC.filler),
  "terminus-font": PackageItemData(IC.filler),
  "testdisk": PackageItemData(IC.filler),
  "tmux": PackageItemData(IC.filler),
  "tpm2-tools": PackageItemData(IC.filler),
  "tpm2-tss": PackageItemData(IC.filler),
  "udftools": PackageItemData(IC.filler),
  "usb_modeswitch": PackageItemData(IC.filler),
  "usbmuxd": PackageItemData(IC.filler),
  "usbutils": PackageItemData(IC.filler),
  "vim": PackageItemData(IC.filler),
  "virtualbox-guest-utils-nox": PackageItemData(IC.filler),
  "vpnc": PackageItemData(IC.filler),
  "wireless-regdb": PackageItemData(IC.filler),
  "wireless_tools": PackageItemData(IC.filler),
  "wpa_supplicant": PackageItemData(IC.filler),
  "wvdial": PackageItemData(IC.filler),
  "xfsprogs": PackageItemData(IC.filler),
  "xl2tpd": PackageItemData(IC.filler)
}

package_groups = {
}

progression_items: Dict[str, str] = [
  ""
]

useful_items = [

]

trap_items = [

]

filler = [

]