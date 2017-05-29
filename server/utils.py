"""
Helper functions for the views
"""

from flask import current_app
from itsdangerous import URLSafeSerializer

def get_serializer(secret_key=None):
    if secret_key is None:
        secret_key = current_app.secret_key
    return URLSafeSerializer(secret_key)
