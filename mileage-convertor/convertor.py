print("Well done how far did ya go there fella?")

# ? Built-in function that asks for user input
# ? and then saves it to a variable
kms = input()
miles = float(kms)/1.60934 # this does the math for kms to miles conversion

# round(thing to round, how many decimal points to round to)

rounded_miles = round(miles, 2) # this rounds the answer of that math to two decimal places

print (f"Well that there { kms } Ki-LO-me-TERS is equal to { rounded_miles } mi-LES ! ! !")
