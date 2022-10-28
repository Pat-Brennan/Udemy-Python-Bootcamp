
class Human:

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = age  # Underscore implies this should be accessed outside of class
        if age >= 0:
            self._age = age
        else:
            self._age = 0

    @property  # This is a decorator! It's a GETTER!
    def age(self):
        return self._age

    @age.setter  # This is a decorator! It's a SETTER!
    def age(self, new_age):
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age cannot be negative!")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


jane = Human("Jane", "Doe", 666)
print(jane)
print(jane.age)  # This prints the GETTER PROPERTY of class HUMAN
jane.age = 420  # This invokes the SETTER PROPERTY of class HUMAN
print(jane.age)  # Prints 420
print(jane.full_name)  # This invokes the FULL_NAME GETTER PROPERTY
jane.full_name = "Bob Ross"
print(jane.full_name)  # Prints Bob Ross
