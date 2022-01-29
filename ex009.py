num = int(input('inform an integer to get its times table 1 to 12:\n'))
print(f'Times Table {num}')
for x in range(0, 12):
    x += 1
    print(f'{num} * {x} = {(num * x)}')

