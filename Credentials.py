"""
This project will create a username and password for the user
"""
import random

class credentials():
    """
    Contains the methods genUsername getUsername
    """
    def genUsername(self) -> str:
        """
        Generates and returns a string username
        """
        chars = "abcdefghijklmnopqrstuvwxyz1234567890_"

        username = ""

        for i in range(16):
            username += random.choice(chars)

        return str(username)
    
    def genPassword(self) -> str:
        """
        Generates and returns a random password if requested
        """
        chars = "abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()"

        password = ""

        for i in range(16):
            password += random.choice(chars)

        return password