print('This program reads the perpendicular sides of a right angle triangle and informs its hypotenus.')
import math
s1 = float(input('Informe the first side: '))
s2 = float(input('Inform the second side: '))
hyp = math.hypot(s1, s2)
print(hyp)
