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
            item = self.__inventory[i]
            if item is not None and item.get_name() == asset_name:
                return self.__inventory.pop(i)
            i += 1
        return None

    def acquire_rig(self, rig_name):
        """Consume a CryptoToken and acquire a new Rig (by name)."""
        if self.__rig is not None:
            print(f"{self.get_name()} already has a rig.")
            return False

        token = self._pick_item("CryptoToken")
        if token is None:
            print(f"{self.get_name()} has no CryptoToken to acquire a rig.")
            return False

        self.__rig = Rig(rig_name)
        print(f"{self.get_name()} activated rig '{self.__rig.get_name()}'.")
        return True

    def store_to_rig(self, asset_name):
        """Move an item from inventory into rig storage (uses Rig.store_asset)."""
        if self.__rig is None:
            print("No rig to store asset.")
            return False

        asset_obj = self._pick_item(asset_name)
        if asset_obj is None:
            print(f"{asset_name} not found in inventory.")
            return False

        # Rig.store_asset expects an Asset instance
        return self.__rig.store_asset(asset_obj)



