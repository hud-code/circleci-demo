from .context import sample

import main

def TestAdd():
        assert main.Add(2,3) == 5
        assert main.Add(2,2) == 4
        assert main.Add(6,7) == 13
        print("Add Function works correctly, with new logic! (part 3, please)")

def TestSub():
        assert main.Subtract(8,5) == 3
        assert main.Subtract(14,5) == 9
        print("Subtract Function works correctly")

def TestMult():
        assert main.Multiply(5,5) == 25
        assert main.Multiply(10,3) == 30
        print("Multiply Function works correctly")

def TestDiv():
        assert main.Divide(5,5) == 1
        assert main.Divide(12,3) == 4
        assert main.Divide(30,0) == None
        print("Divide Function works correctly")

if __name__ == '__main__':
        TestAdd()
        TestSub()
        TestDiv()
        TestMult()