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
