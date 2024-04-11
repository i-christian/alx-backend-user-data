#!/usr/bin/env python3
"""
Module for password hashing and validation.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.

    Args:
        password (str): The password to be hashed.

    Returns:
        bytes: The salted and hashed password as a byte string.
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates a password against its hashed counterpart.

    Args:
        hashed_password (bytes): The hashed password to be validated.
        password (str): The password to be checked for validity.

    Returns:
        bool: True if the password matches the hashed password, else False.
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
