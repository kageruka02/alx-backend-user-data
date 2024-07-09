#!/usr/bin/env python3
""" API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manages the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authetication is required to access path"""
        if path is None or len(excluded_paths) == 0 or excluded_paths is None:
            return True
        if path[-1] != "/":
            path = path + "/"
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization header check"""
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """current user method"""
        return None
