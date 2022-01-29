import random
print('This program reads the names of 4 people, display them in the order informed, shuffle and print them.')

group = []
for x in range(0, 4):
    group.append(input(f'Inform a name of the number {(x + 1)}: '))
print(group)
random.shuffle(group)
print(group)