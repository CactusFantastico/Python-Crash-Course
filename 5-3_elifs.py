age = int(input('Please input your age: '))
if age < 4:
    print('Your admission is free!')
elif age >= 4 and age < 18:
    print('Admission is $5.')
elif age >= 18:
    print('Admission is $10')
else:
    print('Please enter an age!')

age2 = int(input('Please input your age: '))
if age2 < 4:
    price = 0
elif age2 < 18:
    price = 5
else:
    price = 10

print('The price of your admission will be $' + price.__str__() + '.' )
