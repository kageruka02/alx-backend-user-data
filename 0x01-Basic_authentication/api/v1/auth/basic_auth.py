#!/usr/bin/env python3
"""manage the API authentication"""


from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth Class"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if not isinstance(authorization_header, str):
            return None
        index = authorization_header.find(" ")
        if index != -1 and "Basic " in authorization_header:

            return authorization_header[index + 1 :]
        return None
