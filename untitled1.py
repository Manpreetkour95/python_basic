class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def test(self):
      if self.name=="Manpreet":
          print(self.name)
          print("Yes, this function is working")
      if self.age==25:
          print(self.age)
          print("yes, this part is also working")
      
t=Person("Manpreet", 25)
t.age
v=Person("Vikram",29)
v.age

