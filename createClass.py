class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printName(self):
    print('Hello my name is ' + self.name + '\nI am '+ str(self.age) + ' years old')
    
p1 = Person("John", 36)

print(p1.name, p1.age)

p1.printName()
