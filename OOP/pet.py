
# * Class Attributes Continued!

class Pet:

    allowed = ['Cat', 'Dog', 'Fish', 'Rat']  # This is a Class Attribute

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"Sorry your pet is weird and a {species}!")

            self.name = name
            self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"That {species} isn't allowed here!!!")
        self.species = species


cat = Pet("Eorah", "Cat")
dog = Pet("Artie", "Dog")

print(cat)
print(dog)

gator = Pet("Big Chonker", "Gator")

# * Class Methods
# ? Class methods are methods (with the @classmethod decorator) that are not concerned ->
# ? with instances, but the class itself

class User:  # this is what every user will look like

    active_users = 0  # This is a CLASS ATTRIBUTE

@classmethod
def display_active_users(cls): # class is automatically passed in, hence "cls"
    return f"There are currently {cls.active_users} active users"

@classmethod
def from_string(cls, data_str):
    first,last,pet = data_str.split(",")
    return cls(first,last,pet)
    
    # Does not need to be SELF, but it's practical!
    def __init__(self, first, last, pet):
        self.first = first  # These are individual INSTANCES!
        self.last = last
        self.pet = pet
        User.active_users += 1  # This refers to the CLASS ATTRIBUTE

    def logout(self):
        User.active_users -= 1
        return f'{self.first} has logged out!'

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0].upper()}.{self.last[0].upper()}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}!"