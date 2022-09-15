

# * While loops!

# ? Format
# while im_tired:
#     seek caffeine

# ? While loops continue to execute while a certain condition is TRUTHY
# ? and will end when they become FALSY

# user_response = None
# while user_response != "please":
#     user_response = input("WOAH BUDDY?! Say the magic word!!")

# ? While loops require more set up than FOR Loops
# ? since you have to specify the termination conditions manually

# ! Be carful! If the condition never becomes false it will run FOREVER!

print("What's the secret password?") 
msg = input() # ask for input
while msg != 'Anchovies': # while it DOES NOT equal the correct password
    print("Uh oh! That's not smelly enough!")
    msg = input() # ask for input again
print("Welcome to the Fishy Friends!") # All other outcomes result in Fishy Friend Membership
