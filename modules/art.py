
# * ASCII Art Exercise 

from termcolor import colored, cprint
import pyfiglet

result1 = pyfiglet.figlet_format("Turbo", font = 'banner3-d')
result2 = pyfiglet.figlet_format("Team", font = 'banner3-d')
result3 = pyfiglet.figlet_format("!!!!!", font = 'banner3-d')
slogan = pyfiglet.figlet_format("Y O U WALK!", font = '3-d')
colored_result1 = colored(result1, 'red')
colored_result2 = colored(result2, 'white')
colored_result3 = colored(result3, 'blue')
colored_slogan = colored(slogan, 'green')
print(colored_result1)
print(colored_result2)
print(colored_result3)
print(colored_slogan)

# def message (phrase, text_font="slant", color="red"):
#   message = pyfiglet.figlet_format(f'{phrase}', font = f'{text_font}')
#   message_color = colored(message, f'{color}')
#   return message_color
# print(message("I'm alive!","slant", "green"))

valid_colors = ('red', 'green', 'yellow',  'blue', 'magenta', 'cyan')

msg = input("What woudld you like to print? ")
color = input("What color? ")

if color not in valid_colors:
  color = 'magenta'

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii_art = colored(ascii_art, color)
print(colored_ascii_art)