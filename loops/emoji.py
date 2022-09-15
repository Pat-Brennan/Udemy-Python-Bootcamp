
# * Emoji Pyramid

# Use a while loop and a for loop to create an emoji pyramid

# Emoji: print("\U0001f600")

emoji = "😃"

# * For Loop Version

for num in range(1, 11):
    print(emoji * num)

# * While Loop Version

limit = 11
count = 1
while count < limit:
    print(emoji * count)
    count += 1

# * Nested Loop Version

for x in range(3):  # print contents of this loop 3 times
    for number in range(1, 11):  # this will make a pyramid every loop
        print(emoji * number)

# * Another Nested Loop Version

for num in range(1, 11):
    count = 1
    smileys = ""
    while count <= num:
        smileys += "😃"
        count += 1
    print(smileys)
