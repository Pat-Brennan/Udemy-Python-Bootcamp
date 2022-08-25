
# * Bouncer code along!

# ask for age

from re import I


print('What is your age Noble Concert Patron?')
age = input()

if age == '':
  print("I'll ask you one more time friend,")
  print("What is your age?")
  age = input()
elif int(age) < 21 and int(age) >= 18:
    print("No drinking for you friend! A band of caution will be issued!")
elif age >= 21:
    print("Enjoy the show friend! Drink up!")
else:
    print("Thou has not spent enough time on this earth for such entertainment!")


# 18 - 21 wristband
# 21+ to drink, normal entry
# too young, sorry no entry