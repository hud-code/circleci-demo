# Import the Add function, and assert that it works correctly.
from main import Add
from main import Subtract
from main import Multiply
from main import Divide

def TestAdd():
        assert Add(2,3) == 5
        assert Add(2,2) == 4
        assert Add(6,3) == 13 #ERROR HERE
        print("Add Function works correctly, with new logic! (part 3, please)")

def TestSub():
        assert Subtract(8,5) == 3
        assert Subtract(14,5) == 9
        print("Subtract Function works correctly")

def TestMult():
        assert Multiply(5,5) == 25
        assert Multiply(10,3) == 30
        print("Multiply Function works correctly")

def TestDiv():
        assert Divide(5,5) == 1
        assert Divide(12,3) == 4
        assert Divide(30,0) == None
        print("Divide Function works correctly")

if __name__ == '__main__':
        TestAdd()
        TestSub()
        TestMult()
        TestDiv()