class Pet:
   def __init__(self, fur, breed, call):
      self.f=fur
      self.b=breed
      self.c=call
   def eat(self):
      if self.c== "meow":
         print("My darling is eating fish ^3,",self.c)
      elif self.c== "woof":
         print("My darling is eating fish tooo ^3,", self.c)
class Cat(Pet):
   def __init__(self, fur, breed):
       Pet.__init__(self,fur,breed,"meow")
class Dog(Pet):
   def __init__(self, fur, breed):
       Pet.__init__(self, fur, breed, "woof")
myKitti = Cat("White","Siam")
myKitti.eat()
myBoi = Dog("black", "Labrador")
myBoi.eat()