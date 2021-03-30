# Import the Add function, and assert that it works correctly.
from main import Add
from main import Subtract
from main import Multiply
from main import Divide

def TestAdd():
        assert Add(2,3) == 5
        assert Add(2,2) == 4
        print("Add Function works correctly")

def TestSub():
        assert Subtract(8,5) == 3
        assert Subtract(14,5) == 9
        print("Subtract Function works correctly")

def TestMult():
        assert Multiply(5,5) == 25
        assert Multiply(10,3) == 30
        print("Multiply Function works correctly")

def TestDiv():
        assert Divide(5,5) == 25
        assert Divide(10,3) == 30
        assert Divide(30,0) == None
        print("Divide Function works correctly")

if __name__ == '__main__':
        TestAdd()
        TestSub()
        TestMult()
        TestDiv()