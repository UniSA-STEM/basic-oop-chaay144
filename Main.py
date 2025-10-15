"""
File: main.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

#Checking the Asset class
from asset import Asset

token = Asset("CryptoToken", "Used to acquire or repair rigs")
chip = Asset("Security Chip", "Used for encryption and decryption")

print(token)
chip.encrypt()
print(chip)
chip.decrypt()
print(chip)




