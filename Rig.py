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

