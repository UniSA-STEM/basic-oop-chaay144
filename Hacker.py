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

    def acquire_rig(self, rig_name):
        if self.__rig is None:
            token = self._pick_item("CryptoToken")
            if token is not None:
                self.__rig = Rig(rig_name)
                print(f"{self.get_name()} activated rig '{rig_name}'.")
                return True
        return False

    def upgrade_rig(self):
        rig_obj = self.get_rig()
        if rig_obj is None:
            print("No rig found.")
            return False
        if self._blocked():
            print("Trace too high.")
            return False

        patch = self._pick_item("Hardware Patch")
        if patch is None:
            print("No Hardware Patch available.")
            return False

        rig_obj.upgrade()
        return True

    def repair_rig(self):
        rig_obj = self.get_rig()
        if rig_obj is None:
            print("No rig to repair.")
            return False

        token = self._pick_item("CryptoToken")
        if token is None:
            print("No CryptoToken available.")
            return False

        rig_obj.repair()
        return True

    def store_to_rig(self, asset_name):
        rig_obj = self.get_rig()
        if rig_obj is None:
            print("No rig to store asset.")
            return False

        asset_obj = self._pick_item(asset_name)
        if asset_obj is None:
            print(f"{asset_name} not found in inventory.")
            return False

        return rig_obj.store_asset(asset_obj)

    def retrieve_from_rig(self, asset_name):
        rig_obj = self.get_rig()
        if rig_obj is None:
            print("No rig to retrieve asset from.")
            return False

        item = rig_obj.release_asset(asset_name)
        if item is None:
            print(f"{asset_name} not found in rig.")
            return False

        self.__inventory.append(item)
        return True

    def toggle_encryption(self, location, asset_name):
        target_asset = None

        if location == "inventory":
            i = 0
            while i < len(self.__inventory):
                temp = self.__inventory[i]
                if temp is not None and temp.get_name() == asset_name:
                    target_asset = temp
                    break
                i += 1

        elif location == "rig" and self.__rig is not None:
            storage = self.__rig.get_storage()
            j = 0
            while j < len(storage):
                temp = storage[j]
                if temp is not None and temp.get_name() == asset_name:
                    target_asset = temp
                    break
                j += 1

        if target_asset is None:
            print("Asset not found.")
            return False

        if target_asset.encrypted:
            target_asset.decrypt()
        else:
            target_asset.encrypt()
        return True

    def launch_data_spike(self, target: "Hacker"):
        rig_obj = self.get_rig()
        if rig_obj is None:
            print("No rig to launch spike.")
            return False

        spike = rig_obj.release_asset("Data Spike")
        if spike is None:
            print("No Data Spike in rig.")
            return False

        self.__trace_level += 1
        target_rig = target.get_rig()
        if target_rig is not None:
            target_rig.take_hit()
            print(f"{self.get_name()} hit {target.get_name()}'s rig.")
            if target_rig.is_broken():
                self._extract_from_broken(target)
        return True

    def _extract_from_broken(self, target: "Hacker"):
        rig_obj = self.get_rig()
        target_rig = target.get_rig()

        if rig_obj is None or target_rig is None:
            return False

        drive = rig_obj.release_asset("Removable Drive")
        if drive is None:
            print("No Removable Drive.")
            return False

        enemy_storage = target_rig.get_storage()
        i = 0
        while i < len(enemy_storage):
            candidate = enemy_storage[i]
            if candidate is not None and not candidate.encrypted:
                stolen = enemy_storage.pop(i)
                self.__inventory.append(stolen)
                print(f"Extracted {stolen.get_name()} from {target.get_name()}.")
                return True
            i += 1

        print("No unencrypted assets found.")
        return False

    def __str__(self):
        if len(self.__inventory) == 0:
            inv_text = "Empty"
        else:
            inv_text = ""
            i = 0
            while i < len(self.__inventory):
                item = self.__inventory[i]
                if item is not None:
                    inv_text += item.get_name()
                    if i < len(self.__inventory) - 1:
                        inv_text += ", "
                i += 1

        rig_name = self.__rig.get_name() if self.__rig is not None else "None"
        return f"Hacker<{self.__name}> rig={rig_name} trace={self.__trace_level} | Inventory: {inv_text}"