#!/usr/bin/python3
"""This module defibe a single function validUTF8
The function checks if some data is correctly encoded with utf-8
"""


def validUTF8(data):
    """Checks if data is correctly encoded in utf8
    """

    try:
        bytes(data)
        return True
    except Exception:
        return False
