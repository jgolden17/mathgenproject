"""
Utilities
"""
import re

def parse_id(string):
    """
    Parse the mathematician's MGP id from an href string
    """
    return re.compile('id=(.*)').search(string).group(1)

def clean_string(string):
    """
    Clean up a string.

    TODO: This is dumb
    """
    return string\
        .strip('\n\r ')\
        .rstrip('\n\r ')\
        .replace('\n\r', ' ')\
        .replace('\r\n', ' ')\
        .replace('\n', ' ')\
        .replace('\r', ' ')\
        .replace('  ', ' ')
