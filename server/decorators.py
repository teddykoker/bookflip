import functools
from flask import jsonify


def jsonapi(f):
    """This decorator generates an API response from a dictionary or
    model, and a status string."""

    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        status, data = f(*args, **kwargs)

        return jsonify({
            'status': status,
            'data': data
        })

    return wrapped
