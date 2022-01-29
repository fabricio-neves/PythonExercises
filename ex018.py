from math import sin, cos, tan, radians

print('This program reads an angle and return its sin cos and tan.')

angle = float(input('Inform an angle: '))
sine = sin(radians(angle))
cosine = cos(radians(angle))
tangent = tan(radians(angle))

print(f'sen = {sine:.2f}\n'
      f'cos = {cosine:.2f}\n'
      f'tan = {tangent:.2f}')
