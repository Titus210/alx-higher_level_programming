#!/usr/bin/python3
"""Project 3-write_text."""


def write_file(filename="", text=""):
    """"write file"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write(text)
    return len(text)
