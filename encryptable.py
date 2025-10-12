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
    Very small abstract base that says an object must be encryptable.
    This keeps the design clear but stays simple for the assignment.
    """

    @property
    @abstractmethod
    def encrypted(self) -> bool:
        raise NotImplementedError

    @abstractmethod
    def encrypt(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def decrypt(self) -> None:
        raise NotImplementedError