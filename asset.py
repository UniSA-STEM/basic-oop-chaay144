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
        """Mark the asset as encrypted."""
        if not self.encrypted:
            self.encrypted = True
            print(f"{self.name} is now encrypted.")
        else:
            print(f"{self.name} is already encrypted.")

    def decrypt(self):
        """Mark the asset as decrypted."""
        if self.encrypted:
            self.encrypted = False
            print(f"{self.name} has been decrypted.")
        else:
            print(f"{self.name} is already decrypted.")

    def __str__(self):#str name
        if self.encrypted:
            return f"{self.name}: {self.description} [Encrypted]"
        else:
            return f"{self.name}: {self.description}"



