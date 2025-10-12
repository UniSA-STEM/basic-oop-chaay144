"""
File: encryptable.py
Description: <A brief description of this Python module.>
Author: Ansh Channa
ID: 110369235
Username: chaay144
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from abc import ABC, abstractmethod

class Encryptable(ABC):
    """
    This is just a tiny abstract class I made to keep the code a bit more organised.

    """

    @property
    @abstractmethod
    def encrypted(self) -> bool:
        # This makes sure that any class that inherits this has an 'encrypted' state
        raise NotImplementedError

    @abstractmethod
    def encrypt(self) -> None:
        # This will be the method to lock or protect the asset
        raise NotImplementedError

    @abstractmethod
    def decrypt(self) -> None:
        raise NotImplementedError