"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from asset import Asset
from Rig import Rig

TRACE_LIMIT = 5

class Hacker:
    def __init__(self, name):
        self.__name = name
        self.__trace_level = 0
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs.")]
        self.__rig = None

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name

    def get_trace_level(self):
        return self.__trace_level

    def set_trace_level(self, value):
        if isinstance(value, int) and value >= 0:
            self.__trace_level = value

    def get_inventory(self):
        return self.__inventory

    def get_rig(self):
        return self.__rig

    def set_rig(self, rig_obj):
        self.__rig = rig_obj

    def _pick_item(self, asset_name):
        i = 0
        while i < len(self.__inventory):
            current = self.__inventory[i]
            if current is not None and current.get_name() == asset_name:
                return self.__inventory.pop(i)
            i += 1
        return None

    def _blocked(self):
        return self.__trace_level > TRACE_LIMIT