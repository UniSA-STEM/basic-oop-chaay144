"""
File: asset.py
Description: This is my asset file.
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

class Asset:
    # store basic info for each item the hacker can hold
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__encrypted = False # starts unencrypted

    def encrypt(self):
            # mark an asset as encrypted if it’s not already
        if not self.get_encrypted():
            self.__encrypted = True
            print(f"{self.get_name()} is now encrypted.")
        else:
            print(f"{self.get_name()} is already encrypted.")

    def decrypt(self):
        # remove encryption if the asset is currently locked
        if self.get_encrypted():
            self.__encrypted = False
            print(f"{self.get_name()} has been decrypted.")
        else:
            print(f"{self.get_name()} is already decrypted.")


    def get_name(self):
        # return the asset’s name
        return self.__name

    def get_description(self):
        # return what the asset does
        return self.__description

    def get_encrypted(self):
        # check if the asset is encrypted or not
        return self.__encrypted



    def __str__(self):
        # print asset info in a simple readable way
        if self.get_encrypted():
            return f"{self.get_name()}: {self.get_description()} [Encrypted]"
        else:
            return f"{self.get_name()}: {self.get_description()}"



