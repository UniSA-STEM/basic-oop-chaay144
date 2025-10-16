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

    def retrieve_from_rig(self, asset_name):
        """Retrieve an asset from rig storage into inventory (uses Rig.release_asset)."""
        if self.__rig is None:
            print("No rig to retrieve asset from.")
            return False

        item = self.__rig.release_asset(asset_name)
        if item is None:
            print(f"{asset_name} not found in rig.")
            return False

        self.__inventory.append(item)
        return True

    def toggle_encryption(self, location, asset_name):
        """
            Toggle encryption for an asset in 'inventory' or 'rig'.
        """
        target = None

        if location == "inventory":
            target = next((a for a in self.__inventory if a.get_name() == asset_name), None)

        elif location == "rig" and self.__rig is not None:
            storage = self.__rig.get_storage()
            target = next((a for a in storage if a.get_name() == asset_name), None)

        else:
            print("Invalid location or no rig.")
            return False

        if target is None:
            print("Asset not found.")
            return False

        if target.get_encrypted():
            target.decrypt()
        else:
            target.encrypt()
        return True

    def launch_data_spike(self, target_hacker):
        """Use one Data Spike from own rig to hit target_hacker's rig."""
        if self.__rig is None:
            print("No rig to launch spike.")
            return False

        spike = self.__rig.release_asset("Data Spike")
        if spike is None:
            print("No Data Spike in rig.")
            return False

        # increase trace
        self.__trace_level += 1

        target_rig = target_hacker.get_rig()
        if target_rig is not None:
            target_rig.take_hit()
            print(f"{self.get_name()} hit {target_hacker.get_name()}'s rig.")
            if target_rig.is_broken():
                # try extraction if broken
                self._extract_from_broken(target_hacker)
        return True

    def _extract_from_broken(self, target_hacker):
        if self.__rig is None:
            print("No rig to perform extraction.")
            return False

        # try to consume Removable Drive from own rig storage first
        drive = self.__rig.release_asset("Removable Drive")
        if drive is None:
            # try to consume from inventory
            drive = self._pick_item("Removable Drive")
            if drive is None:
                print("No Removable Drive.")
                return False

        target_rig = target_hacker.get_rig()
        if target_rig is None:
            print("Target has no rig.")
            return False

        # search target storage for first unencrypted asset
        storage = target_rig.get_storage()
        i = 0
        while i < len(storage):
            candidate = storage[i]
            if candidate is not None and not candidate.get_encrypted():
                # remove from target storage and add to our inventory
                # use target_rig.release_asset to remove by name
                stolen = target_rig.release_asset(candidate.get_name())
                if stolen:
                    self.__inventory.append(stolen)
                    print(f"Extracted {stolen.get_name()} from {target_hacker.get_name()}.")
                    return True
                else:
                    # if release_asset blocked for some reason, continue
                    i += 1
                    continue
            i += 1

        print("No unencrypted assets found.")
        return False