number=input('Enter a number between 1 and 20: ')
 
if number in ['1','3','5','7','9','11','13','15','17','19']:
 print(number, 'is odd')

elif number in ['2','4','6','8','10','12','14','16','18','20']:
 print(number, 'is even')

else:
    print('Invalid input.')
    