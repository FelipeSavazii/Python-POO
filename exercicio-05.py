class Student:
  __name = None
  __rollNumber = None
  
  def setName(self, name):
    self.__name = name

  def getName(self):
    return self.__name

  def setRollNumber(self, rollNumber):
    self.__rollNumber = rollNumber

  def getRollNumber(self):
    return self.__rollNumber

name = input('Digite o nome: ')
rollNumber = int(input('Digite o número aleatório: '))
  
demo1 = Student()
demo1.setName(name)
print("Nome:", demo1.getName())
demo1.setRollNumber(rollNumber)
print("Número aleatório:", demo1.getRollNumber())
    
