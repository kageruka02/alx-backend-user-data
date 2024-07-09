#!/usr/bin/env python3
"""Manage the API authentication"""

from api.v1.auth.auth import Auth
import base64
from typing import Tuple


class BasicAuth(Auth):
    """BasicAuth Class"""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Returns the Base64 part of the Authorization header"""
        if not isinstance(authorization_header, str):
            return None
        index = authorization_header.find(" ")
        if index != -1 and "Basic " in authorization_header:
            return authorization_header[index + 1:]
        return None

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Decode a Base64 Authorization header"""
        if (
            not isinstance(base64_authorization_header, str)
            or base64_authorization_header is None
        ):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode("utf-8")
        except base64.binascii.Error:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """Returns the user email and password from the Base64 decoded value"""
        if (
            not decoded_base64_authorization_header
            or not isinstance(decoded_base64_authorization_header, str)
            or ":" not in decoded_base64_authorization_header
        ):
            return None, None
        extract = decoded_base64_authorization_header.split(":", 1)
        return (extract[0], extract[1]) if extract else (None, None)
