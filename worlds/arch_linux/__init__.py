from typing import NamedTuple, Union
import logging

from BaseClasses import Item, Tutorial, ItemClassification

from ..AutoWorld import World, WebWorld
from NetUtils import SlotType


class ArchLinuxWeb(WebWorld):
  tutorials = [Tutorial(
    "Setup Guide",
    "A guide for setting up a new Arch Linux live environment as an AP World",
    "English",
    "setup_en.md",
    "setup/en",
    ["🍍"]
  )]

  theme = "partyTime"

