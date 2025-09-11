number=int(input('Enter a number between 0 and 9999:'))
if number<0 or number>9999:
    print('Invalid number! Please enter a number between 0 and 9999.')
else:
    print('Unit: {}'.format(number//1%10))
    print('Tens: {}'.format(number//10%10))
    print('Hundreds: {}'.format(number//100%10))
    print('Thousands: {}'.format(number//1000%10))

