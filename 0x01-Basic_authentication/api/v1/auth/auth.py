#!/usr/bin/env python3
""" API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """manages the API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Check if authetication is required to access path"""
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True
        if path[-1] != "/":
            path += "/"
        for p in excluded_paths:
            if p.endswith("*"):
                if path.startswith(p[:1]):
                    return False
        return False if path in excluded_paths else True

    def authorization_header(self, request=None) -> str:
        """authorization header check"""
        if request is None:
            return None
        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar("User"):
        """current user method"""
        return None
    
if __name__ == '__main__':
    a = Auth()

