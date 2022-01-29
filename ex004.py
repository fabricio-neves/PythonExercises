a = input('Type something:\n')
print(f'{a} is:')
if a.isalnum():
    print('Alphanumeric')
if a.isalpha():
    print('Alphabetic')
if a.isascii():
    print('ASCII')
if a.isdecimal():
    print('Decimal')
if a.isdigit():
    print('Digit')
if a.isidentifier():
    print('Valid Python Identifier')
if a.islower():
    print('Lowercase')
if a.isnumeric():
    print('Numeric')
if a.isprintable():
    print('printable')
if a.isspace():
    print('Whitespace')
if a.istitle():
    print('Title-cased')
if a.isupper():
    print('Uppercase')