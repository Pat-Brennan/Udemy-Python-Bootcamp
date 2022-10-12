import sys

from termcolor import colored, cprint
import termcolor

text = colored('hello world!', 'cyan', 'on_magenta', ['bold', 'blink'])
print(text)


def print_red_on_cyan(x): return cprint(x, 'red', 'on_cyan')


print_red_on_cyan("I'm alive!!!")

help(termcolor)
