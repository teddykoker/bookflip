"""
Helper functions for the views
"""

from flask import jsonify


def api_response(status, data=None):
    return jsonify({
        'status': status,
        'data': data
    })
