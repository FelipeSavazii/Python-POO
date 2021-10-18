class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sqx = self.x * self.x
        sqy = self.y * self.y
        sqz = self.z * self.z
        return(sqx +  sqy + sqz) 
     
x = int(input('Digite o X: '))
y = int(input('Digite o Y: '))
z = int(input('Digite o Z: '))

resultado = Point(x, y, z)
print(resultado.sqSum())
