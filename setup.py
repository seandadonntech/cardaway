import os
task = input("Do you want to install all packages require for this respo? type help to see commands[+]\n")

if task =="1":
    os.system("pip install pyfiglet")
    os.system("pip install colorama")
    os.system("pip install credit_card_checker")
    os.system("pip install time")
    print("All set all packages installed !")
if task =="2":
 print("ok you dont want to install program closed")

if task == "3":
 os.system("pip uninstall pyfiglet")
 os.system("pip uninstall colorama")
 os.system("pip uninstall credit_card_checker")
 os.system("pip uninstall time")
 print("ok everything uninstalled")
elif task =="help":
 print("Enter 1 to install packages 2 you dont and 3 for help ")

else:
 print("invalid command")
#this program will install the need requirements
