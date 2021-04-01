

def Add(a, b):
        return a + b

def Subtract(a, b):
        return a - b

def Multiply(a, b):
        return a * b

def Divide(a, b):
        if b > 0:
                return a / b
        else:
                return None

def Square(a):
        return a * a


def SayHello():
        print("Hello World!")

if __name__ == '__main__':
        SayHello()