from credit_card_checker import CreditCardChecker

input = input("whats your credit card number?")
card = CreditCardChecker(f'{input}').valid()
print("notice if the number you type is true the card is correct otherwise its wrong or you didnt type something right!")
print(card)

