from .context import sample

import main

import unittest

def TestSquare():
    assert main.Add(4) == 16
    assert main.Add(5) == 25
    print("This is test 2 and Square works correctly!")

if __name__ == '__main__':
    TestSquare()