print('This program calculate the amount of paint needed to paint a wall given its width and height.')
w = int(input('Inform the width in meters: '))
h = int(input('Inform the height in meters: '))
rate = 2
total = w * h / rate
print(f'With a paint that paints {rate} square meters per liter, you can paint your wall with {total} liters.')
