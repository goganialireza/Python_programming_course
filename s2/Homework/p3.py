a = float(input('a?'))
b = float(input('b?'))
c = float(input('c?'))

m = (a + b + c) / 3

if m < 0:
    print('m is negative')
elif 0 <= m <= 10:
    print('m is between 0 to 10')
elif 11 <= m <= 20:
    print('m is between 11 to 20')
elif m > 20:
    print('m is bigger than 20')
