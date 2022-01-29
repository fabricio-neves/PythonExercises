from random import choice

print('This program reads the names of 4 students and pics one randomly.')
students = []
for x in range(0, 4):
    students.append(input(f'Inform the name of the student {(x+1)}: '))
print(choice(students))
