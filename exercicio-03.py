class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return(self.num1 + self.num2)

    def subtract(self):
        return(self.num2 - self.num1)

    def multiply(self):
        return(self.num1 * self.num2)

    def divide(self):
        return(self.num2 / self.num1)

num1 = int(input('Digite o num1: '))
num2 = int(input('Digite o num2: '))

calculator = Calculator(num1, num2)
print("Adição:", calculator.add())
print("Subtração:", calculator.subtract())
print("Mutiplicação:", calculator.multiply())
print("Divisão:", calculator.divide())
