class GrumpyDict(dict):
  def __repr__(self):
    print("Kick rocks, Chump!")
    return super().__repr__()
  
  def __missing__(self, key):
    print(f"You wanted {key}?! Well it aint here!")
  
  def __setitem__(self, key, value):
    print("you want me to do WHAT now?!")
    print("Well, alright.")
    super().__setitem__(key, value)

data = GrumpyDict({ 'first':'Eorah', 'last':'The Destroyer', 'animal':'Demon' })
print(data)
data['city'] = 'Planet Terror'
print(data)