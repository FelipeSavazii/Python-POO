class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return(self.__length * self.__width)

    def perimeter(self):
        return(2 * (self.__length + self.__width))

length = int(input('Digite o comprimento: '))
width = int(input('Digite a largura: '))

retangulo = Rectangle(length, width)
print("A área é", retangulo.area())
print("O perimetro é", retangulo.perimeter())
