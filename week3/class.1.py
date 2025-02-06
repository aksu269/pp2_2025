class MyClass:
    def __init__ (self):
        self.string = ''
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())
p1 = MyClass()
p1.getString()
p1.printString()