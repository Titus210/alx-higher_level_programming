#!/usr/bin/python3
"""Project 3-write_text.py
Write text to a file
"""


def write_file(filename="", text=""):
    """
    Writting file to a fiile and creates one if it exists

    Args:
        - filename: name of file
        - text: string to be written on file

    Returns: characters written
    """

    with open("my_first_file.txt","w+",encoding = "uft-8") as f:
        return f.write(text)
