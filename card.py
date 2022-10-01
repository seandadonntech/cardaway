from credit_card_checker import CreditCardChecker
from colorama import Fore, Back, Style
print(Fore.GREEN + 'A  program that genrates text into pyfiglet  made by seandadonntech , technio#7716, Copyright (c) 2022, lilcryptotech All rights reserved. ')
input = input("whats your credit card number?")
card = CreditCardChecker(f'{input}').valid()
print("notice if the number you type is true the card is correct otherwise its wrong or you didnt type something right!")
print(card)
# if you are going to be using this for recording or any public use please use the copyright thank you!
