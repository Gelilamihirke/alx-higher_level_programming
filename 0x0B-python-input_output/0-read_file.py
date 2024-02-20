#!/usr/bin/python3
"""Defines function."""
def read_file(filename=""):
    """Print the contents"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
