

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

# * Infinite Loop! 

# num = 1
# while num < 11: # Num will always be less than 11
#   print(num)

# * Solution to above!

# num = 1 
# while num < 11:
#   print(num)
#   num += 1 # 1 will eventually increment to be more than 11

# * For Loop verstion of above!

# for num in range(1, 11):
#   print(num)

# ? range() replaces the need to increment by 1

# * BREAK Keyword

# ? The keyword break gives us the ability to exit out of WHILE LOOPS whenever we want

while True:
    command = input("Type 'exit' to exit: ")
    if command == "exit": # When exit is typed
        break # the while loop will stop

# ? We can also use it to end FOR LOOPS early

for x in range(1, 111):
    print(x)
    if x == 3: # when the range hits 3
        break # the while loop will stop
    
# * Adding a break

times = int(input('How many times do I have to tell you?!'))

for time in range(times):
    print('CLEAN YOUR ROOM!')
    if times >= 4:
        print('Do you even listen anymore??')
        break