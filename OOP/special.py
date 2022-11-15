class Human:
  def __init__(self, first, last, age):
    self.first = first
    self.last = last
    self.age = age
  
  def __repr__(self):
    return f"Human named {self.first} {self.last}"
  
  def __len__(self):
    return self.age
  
  def __add__(self, other):
    if isinstance(other, Human):
      return Human(first="Newborn", last=self.last, age=0)
    return TypeError("You can't add that!")
  
  def __mul__(self, other):
    if isinstance(other, int):
      return [self for i in range(other)]
    return TypeError("You can't Clone that!")

j = Human("Big", "Chungus", 3000)
k = Human("Garfield", "The Cat", 666)
print(j)
print(len(j))
print(j + k)
print(j * 3)
