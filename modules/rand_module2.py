
# * The 'from' Keyword
# ? This is used when you only want a PART of the module, instead of the whole thing!

from random import choice, randint

# ? Notice, we no longer need to place the 'random', in front of choice or randint ...

print(choice(['banana', 'pepper', 'pudding']))
print(randint(1, 666))

# ? from random import *
# ? The * brings in all of the random modules
# ? You can technically do this but frowned upon
