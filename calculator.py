# calculator.py
class Calculator:
    def __init__(self):
        print("Calculator initialized")

    def calculate(self, operation, a, b):
        if operation == "add":
            return self.add(a, b)

    def add(self, a, b):
        return a + b

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to Calculator!")
