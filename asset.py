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
        self.__name = name
        self.__description = description
        self.__encrypted = False

    def encrypt(self):
        """Mark the asset as encrypted."""
        if not self.get_encrypted():
            self.__encrypted = True
            print(f"{self.get_name()} is now encrypted.")
        else:
            print(f"{self.get_name()} is already encrypted.")

    def decrypt(self):
        """Mark the asset as decrypted."""
        if self.get_encrypted():
            self.__encrypted = False
            print(f"{self.get_name()} has been decrypted.")
        else:
            print(f"{self.get_name()} is already decrypted.")


    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def get_encrypted(self):
        return self.__encrypted



    def __str__(self):#str name
        if self.get_encrypted():
            return f"{self.get_name()}: {self.get_description()} [Encrypted]"
        else:
            return f"{self.get_name()}: {self.get_description()}"



