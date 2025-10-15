"""
File: main.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""


from asset import Asset
from Rig import Rig

#Checking the Asset class
token = Asset("CryptoToken", "Used to acquire or repair rigs")
chip = Asset("Security Chip", "Used for encryption and decryption")

print(token)
chip.encrypt()
print(chip)
chip.decrypt()
print(chip)



#Checking the Rig class
r = Rig("CyberDeck")
token = Asset("CryptoToken", "Used to buy rigs")
chip = Asset("Security Chip", "For encryption")
chip.encrypt()

r.store_asset(token)   # should store
r.store_asset(chip)    # should block (encrypted)
r.release_asset("CryptoToken")  # should release
r.release_asset("Security Chip")  # should block
print(r)



