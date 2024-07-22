#!/usr/bin/env python3
"""Module for authentication.
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    "hashing a password"
    password = password.encode()
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password, salt)
