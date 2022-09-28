#!/usr/bin/python3
"""Module 0-read_file.py
Reading from a file and prints
"""
def read_file(filename=""):
    """Read a file and prints it out stdout"""
    with open(filename, "r", encoding= "uft-8") as f:
        print(f.read(), end="")
