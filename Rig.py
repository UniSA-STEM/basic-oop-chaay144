"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""
import random
from asset import Asset
class Rig:
    def __init__(self, name):
        self.__name = name
        self.__damage = 0
        self.__broken = False
        self.__upgrade_level = 0
        self.__storage=[Asset("Data spike","Used in attacks"),
                      Asset("Data Spike", "Used in attacks"),
                      Asset("Removable Drive", "Used to extract assets")
                      ]

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name is not None and isinstance(new_name, str):
            self.__name = new_name

    def get_damage(self):
        return self.__damage

    def set_damage(self, value):
        if value >= 0:
            self.__damage = value

    def is_broken(self):
        return self.__broken

    def set_broken(self, state):

        self.__broken = state

    def get_upgrade_level(self):
        return self.__upgrade_level

    def set_upgrade_level(self, level):
        if level >= 0:
            self.__upgrade_level = level

    def get_storage(self):
        return self.__storage

    def generate_asset(self):
        asset_pool = [
            ("CryptoToken", "Used to acquire or repair rigs. (H)"),
            ("Data Spike", "Used in battles. (R)"),
            ("Removable Drive", "Found in rigs and used for extraction. (R)"),
            ("Security Chip", "Used to encrypt or decrypt assets. (H or R)"),
            ("Hardware Patch", "Used to upgrade rigs. (H)")
        ]

        item = random.choice(asset_pool)
        new_asset = Asset(item[0], item[1])
        self.get_storage().append(new_asset)

        print(f"Rig generated new asset: {new_asset.get_name()}")
        return new_asset

    def condition(self):
        """Return condition string based on damage and upgrade level."""
        if self.is_broken():
            return f"Broken (Level {self.get_upgrade_level()})"
        elif self.__damage == 0:
            return f"Pristine (Level {self.get_upgrade_level()})"
        else:
            return f"Damaged (Level {self.get_upgrade_level()})"

    def store_asset(self, asset):
        """
        Add an asset to rig storage (if not encrypted).
        Returns True if stored, False if blocked.
        """
        if asset.encrypt:
            print(f"{asset.name} is encrypted and cannot be stored.")
            return False

        self.get_storage().append(asset)
        print(f"{asset.name} stored in {self.get_name()}.")
        return True

    def release_asset(self, asset_name):
        """Remove and return an asset from storage by name."""
        for asset in self.get_storage():
            if asset.get_name() == asset_name:
                if asset.encrypt:
                    print(f"{asset.get_name()} is encrypted and cannot be released.")
                    return None
                self.get_storage().remove(asset)
                print(f"{asset.get_name()} released from {self.get_name()}.")
                return asset
        print(f"{asset_name} not found in {self.get_name()}.")
        return None

    def upgrade(self):
        """Increase the rig's upgrade level."""
        self.__upgrade_level += 1
        print(f"{self.get_name()} upgraded to Level {self.get_upgrade_level()}.")

    def repair(self):
        """Repair the rig if damaged (cost logic handled by Hacker)."""
        if self.__broken or self.get_damage() > 0:
            self.__damage = 0
            self.__broken = False
            print(f"{self.get_name()} has been repaired and is now functional.")
        else:
            print(f"{self.get_name()} does not need repairs.")

    def take_hit(self):
        """Increase rig damage; mark broken if limit reached."""
        if not self.is_broken():
            self.__damage += 1
            print(f"{self.get_name()} took a hit! Damage: {self.get_damage()}")

            # Simple rule: damage 2 breaks level 0 rig
            if self.__damage >= 2 and self.__upgrade_level == 0:
                self.__broken = True
                print(f"{self.get_name()} is now broken!")
        else:
            print(f"{self.get_name()} is already broken.")

    def __str__(self):
        if len(self.__storage) == 0:
            stored_names = "Empty"
        else:
            stored_names = ""
            i = 0
            while i < len(self.__storage):
                asset = self.__storage[i]
                stored_names += asset.get_name()
                if i < len(self.__storage) - 1:
                    stored_names += ", "
                i += 1

        return f"Rig: {self.__name} | {self.condition()} | Stored: [{stored_names}]"