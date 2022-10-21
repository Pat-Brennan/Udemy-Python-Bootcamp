
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
