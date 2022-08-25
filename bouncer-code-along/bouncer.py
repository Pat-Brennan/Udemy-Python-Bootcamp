
# * Bouncer code along!

# ask for age
print('What is your age Noble Concert Patron?')
age = input()

if age != '':
    age = int(age)
    if age < 21 and age >= 18:
      print("No drinking for you friend! A band of caution will be issued!")
    elif age >= 21:
        print("Enjoy the show friend! Drink up!")
    else:
        print("Thou has not spent enough time on this earth for such entertainment!")
else:
    print("I'll ask you one more time friend,")
    print("What is your age?")

# ? Refactored
# if age:
#     age = int(age)
#     if age >= 21:
#         print("Enjoy the show friend! Drink up!")
#     elif age >= 18:
#         print("No drinking for you friend! A band of caution will be issued!")
#     else:
#         print("Thou has not spent enough time on this earth for such entertainment!")
# else:
#     print("Please enter an Age!")
