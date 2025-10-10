"""
File: Asset.py
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
        """Marks the asset as encrypted."""
        self.encrypted = True

    def decrypt(self):
        """Marks the asset as decrypted."""
        self.encrypted = False

    def display(self):
        """Displays the asset information clearly."""
        if self.encrypted:
            print(f"{self.name}: {self.description} [Encrypted]")
        else:
            print(f"{self.name}: {self.description}")
