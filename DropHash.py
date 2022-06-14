from asyncore import loop
import enum
from itertools import count
import os
import string
from posixpath import split
import random
import time
import json
import colorama
from colorama import Fore, Back, Style

print('\033[31m' + '''
  ██████╗ ██████╗  ██████╗ ██████╗ ██╗  ██╗ █████╗ ███████╗██╗  ██╗
  ██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██║  ██║██╔══██╗██╔════╝██║  ██║
  ██║  ██║██████╔╝██║   ██║██████╔╝███████║███████║███████╗███████║
  ██║  ██║██╔══██╗██║   ██║██╔═══╝ ██╔══██║██╔══██║╚════██║██╔══██║
  ██████╔╝██║  ██║╚██████╔╝██║     ██║  ██║██║  ██║███████║██║  ██║
  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
''')
def hashing():
  print('\033[39m' + "Welcome to drop's randomized hashing algorithm!\nmeaning the input will never give the same output")
  tohash = input("Please Input a string to hash: ")
  def split(tohash):
    return [char for char in tohash]
  input("\nPress Enter to continue the program\n")
  time.sleep(2)
  os.system('cls')
  os.system('clear')

################
## Split Chars #
################

  print(">>> Hello! This is the string you want hashed:\n")
  print(split(tohash))

#################
## Count Chars ##
#################

  print("\nWhich is this many characters long.\n")
  print(len(tohash))
  print("\n>>> The Following characters will be your encoded string!\n")
  print("")
  numbers = '1', '2', '3', '4', '5', '6', '7', '8', '9'
  characters = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'

#############
## Hashing ##
#############

  with open(f"{tohash}.txt", "w") as f:
    for _ in range(len(tohash)):
      print(random.choice(numbers) + random.choice(characters))
      f.write(random.choice(numbers) + random.choice(characters) + "\n")

  input(" \nPress Enter to terminate the program\n")
  print("See you later.")

hashing()
