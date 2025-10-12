"""
File: asset.py
Description: This is my asset file.
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.encrypted = False

    def encrypt(self):
        self.encrypted = True

    def decrypt(self):
        self.encrypted = False

    def get_encrypted(self):
        return self.encrypted

    def __str__(self):#str name
        if self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        else:
            return f"{self.name}: {self.description}"



