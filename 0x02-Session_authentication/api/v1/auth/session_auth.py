#!/usr/bin/env python3
""" Session authentication
"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    "Session authentication"
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        "create session return session_id"
        if not user_id:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        "get the value of session_id"
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a User instance based on a cookie value"""
        session_id = self.session_cookie(request)
        if session_id is None:
            return None
        user_id = self.user_id_for_session_id(session_id)
        return User.get(user_id)

    def destroy_session(self, request=None):
        "destroy the session"
        if not request:
            return False
        session_id = self.session_cookie(request)
        if not session_id:
            return False
        user_id = self.user_id_for_session_id(session_id)

        if not user_id:
            return False

        try:
            del self.user_id_by_session_id[session_id]
        except Exception:
            pass

        return True
