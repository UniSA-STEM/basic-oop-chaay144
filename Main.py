"""
File: main.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from security_chip import SecurityChip

c = SecurityChip(uses=2)
print(c, c.has_charge())
print("use1:", c.use(), "remaining:", c.uses)
print("use2:", c.use(), "remaining:", c.uses)
print("use3:", c.use(), "remaining:", c.uses)


