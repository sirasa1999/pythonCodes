#leap_year

def leap_year():
    year=int(input('Enter a year'))
    if year%4==0:
        print('It is a leap year.')
    else:
        print('It is not a leap year.')

leap_year()
