"""
File: security.py
Description: <A brief description of this Python module.>
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

# security_chip.py

class SecurityChip:
    """
    A very small security chip object.
    It has a limited number of uses and can be consumed to allow encrypt/decrypt actions.
    """

    def __init__(self, uses: int = 1):
        self.uses: int = int(uses)

    def has_charge(self) -> bool:
        """Return True if the chip still has uses left."""
        return self.uses > 0

    def use(self) -> bool:
        """
        Consume one use if available.
        Returns True if a use was consumed, False if the chip was empty.
        """
        if self.has_charge():
            self.uses -= 1
            return True
        return False

    def __repr__(self) -> str:
        return f"SecurityChip(uses={self.uses})"
