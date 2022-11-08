
# * Polymorphism!
# ? A key principle in OOP is the idea polymorphism - an object can take on many (poly) forms (morph)
# ? Practical Application: 
# ? 1.) The same class method works in a similar way for different classes.
# ? 2.) The same operation works for different kinds of objects.

class Animal():
  def speak(self):
    return NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
  def speak(self):
    return "Woof!"

class Cat(Animal):
  def speak(self):
    return "Destroy all humans!"

class Fish(Animal):
  def speak(self):
    return "Rubba glub glub!"
  
d = Dog()
print(d.speak())
f = Fish()
print(f.speak())