#!/usr/bin/env python3
""" API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manages the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authetication is required to access path"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorization header check"""
        return None

    def current_user(self, request=None) -> TypeVar("User"):
        """current user method"""
        return None
