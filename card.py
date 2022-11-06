from credit_card_checker import CreditCardChecker
from time import *
from colorama import Fore
print(Fore.GREEN + 'A  program that genrates text into pyfiglet  made by seandadonntech , technio#7716, Copyright (c) 2022, lilcryptotech All rights reserved. ')


input = input("Enter a card number or type help:\n")
card = CreditCardChecker(f'{input}').valid()
print("notice if the number you type is true the card is correct otherwise its wrong or you didnt type something right!")
print(card)# this function would is to return the value of the card as true or flase
if input == "help":
 print("A program to check if card is valid or not made by seandadonntech/lilcryptotech/technio#7716")
if card == True: #if card is true the number is correct  or valid
 print(f"{input} is a valid card number")
elif card == False: # if card is
 print(f" {input} is not a card number")

else:
 print(f" {input}  this number is not valid at all ")
#add loop when i get home so program could restart
#this is the github version pls don't forget to add the copy right
#sooon program would see the card bank
sleep(150)
#sleep functions makes sure your shit wont close
