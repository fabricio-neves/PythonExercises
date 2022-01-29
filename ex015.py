print('This program calculates the total amount due for a car rent.')
day_price = 60
distance_price = 0.15
days = int(input('How many days did you keep the car? '))
distance = float(input('How many kilometers did you drive with the car? '))
total = day_price * days + distance_price * distance
print(f'The total amount due is €{total:.2f}')
