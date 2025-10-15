"""
File: Hacker.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from asset import Asset


class Hacker:
    def __init__(self, name):
        self.name = name
        self.trace_level = 0
        self.inventory = [Asset("Crypto_token", "Used to acquire  or repair rigs")]
        self.rig = None

