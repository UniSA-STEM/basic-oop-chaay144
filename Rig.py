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
    def __init__(self, name: str):
        self.name: str = name
        self.damage: int = 0
        self.broken: bool = False
        self.upgrade_level: int = 0
        self.storage=[Asset("Data spike","used in"),
                      Asset("Data Spike", "Used in attacks"),
                      Asset("Removable Drive", "Used to extract assets")
                      ]

    def condition(self):
        if self.broken:
            return f"Broken (Level {self.upgrade_level})"
        if self.damage == 0:
            return f"Pristine (Level {self.upgrade_level})"
        return f"Damaged (Level {self.upgrade_level})"

    def __str__(self):
        if not self.storage:
            item_list = "Empty Rig"
        else:
            item_list = ""
            i = 0
            while i < len(self.storage):
                item_list += self.storage[i].__str__()
                if i < len(self.storage) - 1:
                    item_list += ", "
                i += 1

        return f"Rig Name: {self.name} | {self.condition()} | Assets stored: {item_list}"

    def store(self, asset_obj: Asset):
        if asset_obj.get_encrypted():
            print("you have to decrypt asset before storing it")
            return
        self.storage.append(asset_obj)
        print("Success! Rig storage stored asset")
