from animals.exceptions import ValidException
import re


def valid_latitude(value):
    if value < -90.0 or value > 90.0 or value is None:
        raise ValidException()


def valid_longitude(value):
    if value < -180.0 or value > 180.0 or value is None:
        raise ValidException()


def valid_id(value):
    reg = re.compile('(?<![-.])\b(?!0+)[0-9]+\b(?!\b.[0-9])')
    if not reg.match(value):
        raise ValidException()


def valid_type(value):
    if value is None or value == " " or value == "":
        raise ValidException()
