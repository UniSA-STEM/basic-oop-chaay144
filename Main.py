"""
File: main.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from asset import Asset
from Hacker import Hacker

print("\n=== Into the Grid — Minimal Run (Ansh vs Rival) ===\n")

# Creating the hackers
ansh = Hacker("Ansh")
rival = Hacker("Rival")

# Seed inventories with extra assets so flows can run
ansh.get_inventory().extend([
    Asset("Hardware Patch", "Used to upgrade rigs."),
    Asset("Security Chip", "Used to encrypt/decrypt assets."),
    Asset("CryptoToken", "Used to acquire or repair rigs.")  # extra token
])

rival.get_inventory().extend([
    Asset("Hardware Patch", "Used to upgrade rigs."),
    Asset("CryptoToken", "Used to acquire or repair rigs."),
    Asset("CryptoToken", "Backup token.")
])

# Each acquires a rig
ansh.acquire_rig("AnshFrame")
rival.acquire_rig("RivalCore")

print(ansh)
print(rival)
print(ansh.get_rig())
print(rival.get_rig())

# Upgrade both rigs
ansh.upgrade_rig()
rival.upgrade_rig()
print("\nAfter upgrades:")
print(ansh.get_rig())
print(rival.get_rig())

# Populate storages with several assets (no store/release calls; append directly)
ansh.get_rig().get_storage().extend([
    Asset("Data Spike", "Used in battles."),
    Asset("Removable Drive", "Used to extract assets"),
    Asset("Repair Kit", "Spare repair supplies"),
    Asset("Core Fragment", "Minor valuable fragment")
])

rival.get_rig().get_storage().extend([
    Asset("Data Spike", "Used in battles."),
    Asset("Removable Drive", "Used to extract assets"),
    Asset("Encrypted Log", "Sensitive logs"),
    Asset("Sector Map", "Useful navigation data")
])

# Encrypt one of Rival's assets to show it won't be stolen
for a in rival.get_rig().get_storage():
    if a.get_name() == "Encrypted Log":
        a.encrypt()
        break

print("\n-- Before first fight --")
print(ansh.get_rig())
print(rival.get_rig())

# First fight: Ansh attacks Rival twice
ansh.launch_data_spike(rival)
ansh.launch_data_spike(rival)

print("\n-- After first fight --")
print(ansh)
print(ansh.get_rig())
print(rival.get_rig())

# Rival prepares a counter-attack: add spikes to Rival's rig storage
rival.get_rig().get_storage().append(Asset("Data Spike", "Used in battles."))
rival.get_rig().get_storage().append(Asset("Data Spike", "Used in battles."))
rival.get_rig().get_storage().append(Asset("Removable Drive", "Used to extract assets"))

print("\n-- Rival counter-attacks --")
rival.launch_data_spike(ansh)
rival.launch_data_spike(ansh)

print("\n-- After counter-attack --")
print(rival)
print(rival.get_rig())
print(ansh.get_rig())

# Trace threshold demonstration: push Ansh trace high then attempt an upgrade
print("\n-- Forcing Ansh's trace above limit --")
for _ in range(6):
    # ensure there is a spike to use
    ansh.get_rig().get_storage().append(Asset("Data Spike", "Used in battles."))
    ansh.launch_data_spike(rival)

print(f"Ansh trace level: {ansh.get_trace_level()}")
ansh.get_inventory().append(Asset("Hardware Patch", "Used to upgrade rigs."))
ansh.upgrade_rig()  # should be blocked if trace > limit

# Repair demonstration for both rigs
print("\n-- Repair attempts --")
ansh.get_rig().take_hit()
ansh.repair_rig()  # may fail if no CryptoToken
ansh.get_inventory().append(Asset("CryptoToken", "Used to acquire or repair rigs."))
ansh.repair_rig()

rival.get_rig().take_hit()
rival.repair_rig()  # may succeed if rival has token

print("\n=== Run complete ===\n")
