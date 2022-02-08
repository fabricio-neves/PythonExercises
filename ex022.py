print('This program reads your full name, and analyse it.')
full_name = input('Inform your full name: ')
# full_name = str(input('inform your full name: ')).strip
print('Analysing your name...')
print(f'Your name is written in upper case as {full_name.upper()}.')
print(f'Your name is written in lower case as {full_name.lower()}.')
print(f'Your full name has {len(full_name) - full_name.count(" ")} characters.')
print(f'Your first name is {full_name.split()[0]} and it has {len(full_name.split()[0])}.')
