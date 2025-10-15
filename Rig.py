"""
File: Rig.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from asset import Asset
class Rig:
    def __init__(self, name):
        self.name = name
        self.damage = 0
        self.broken = False
        self.upgrade_level = 0
        self.storage=[Asset("Data spike","Used in attacks"),
                      Asset("Data Spike", "Used in attacks"),
                      Asset("Removable Drive", "Used to extract assets")
                      ]

    def condition(self):
        """Return condition string based on damage and upgrade level."""
        if self.broken:
            return f"Broken (Level {self.upgrade_level})"
        elif self.damage == 0:
            return f"Pristine (Level {self.upgrade_level})"
        else:
            return f"Damaged (Level {self.upgrade_level})"

    def store_asset(self, asset):
        """
        Add an asset to rig storage (if not encrypted).
        Returns True if stored, False if blocked.
        """
        if asset.encrypt:
            print(f"{asset.name} is encrypted and cannot be stored.")
            return False

        self.storage.append(asset)
        print(f"{asset.name} stored in {self.name}.")
        return True

    def release_asset(self, asset_name):
        """Remove and return an asset from storage by name."""
        for asset in self.storage:
            if asset.name == asset_name:
                if asset.encrypt:
                    print(f"{asset.name} is encrypted and cannot be released.")
                    return None
                self.storage.remove(asset)
                print(f"{asset.name} released from {self.name}.")
                return asset
        print(f"{asset_name} not found in {self.name}.")
        return None

    def upgrade(self):
        """Increase the rig's upgrade level."""
        self.upgrade_level += 1
        print(f"{self.name} upgraded to Level {self.upgrade_level}.")

    def repair(self):
        """Repair the rig if damaged (cost logic handled by Hacker)."""
        if self.broken or self.damage > 0:
            self.damage = 0
            self.broken = False
            print(f"{self.name} has been repaired and is now functional.")
        else:
            print(f"{self.name} does not need repairs.")

    def take_hit(self):
        """Increase rig damage; mark broken if limit reached."""
        if not self.broken:
            self.damage += 1
            print(f"{self.name} took a hit! Damage: {self.damage}")

            # Simple rule: damage 2 breaks level 0 rig
            if self.damage >= 2 + self.upgrade_level:
                self.broken = True
                print(f"{self.name} is now broken!")
        else:
            print(f"{self.name} is already broken.")

    def __str__(self):
        """Readable string for the rig's status."""
        stored = ", ".join([asset.name for asset in self.storage])
        return (
            f"Rig: {self.name} | {self.condition()} | "
            f"Stored: [{stored if stored else 'Empty'}]"
        )