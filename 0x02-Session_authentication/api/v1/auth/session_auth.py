#!/usr/bin/env python3
""" Session authentication
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    "Session authentication" 
    pass
