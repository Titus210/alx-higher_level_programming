#!/usr/bin/python3
"""Load_to_json_file"""
import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
