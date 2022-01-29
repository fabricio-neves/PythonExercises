def exchanger(money, rate):
    #    money = input(f'How much {currency} do you want to exchange to dollar?')
    exchange = float(money) * rate
    return exchange


'''
menu = input('type the number associated to the currency from you want to make an exchange to dollar?\n'
             '1. Euro (EUR)'
             '2. Reais (BRL)')
'''
# currency = 'euro'
amount = input('Inform the amount of euros dou you want to exchange for dollar?\n')
euro_rate = 1.13
change = exchanger(amount, euro_rate)
print(f'For the amount of {amount} euros you can get {change:.2f}')
