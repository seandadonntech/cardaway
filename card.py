from credit_card_checker import CreditCardChecker
from time import *
import pyfiglet
from colorama import Fore

print(Fore.GREEN + 'A  program made to check to see if A card number is valid  made by seandadonntech , technio#7716, Copyright (c) 2022, lilcryptotech All rights reserved. ')
print('-' * 129)
result = pyfiglet.figlet_format("card number checker", font = "slant" )
print(result)

print("-"* 129)

input = input("Enter a card number or type help:\n")
card = CreditCardChecker(f'{input}').valid()
print("notice if the number you type is true the card is correct otherwise its wrong or you didnt type something right!")
print(card)# this function would is to return the value of the card as true or flase
if input == "help":
 print("A program to check if card is valid or not made by seandadonntech/lilcryptotech/technio#7716")
if card == True: #if card is true the number is correct  or valid
 print(f"{input} is a valid card number")
elif card == False: # if card is
 print(Fore.RED + f" {input} is not valid number")#this wouls never ben used
else:
 print(Fore.YELLOW + f" {input}  this is not a card number at all ") # this part may not work


#add loop when i get home so program could restart
#sooon program would see the card bank
sleep(150)


