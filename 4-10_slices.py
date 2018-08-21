cars = ['toyota', 'honda', 'audi', 'bmw', 'hyundai']
#  slice the first three
print('the first three items in the list are: ')
print(cars[:3])

# slice the middle three
print('\nThe middle three items in the list are:')
print(cars[1:4])

#  slice the last 3
print('\nThe last three items on the list are:')
print(cars[2:])

#  copy a list but keep it independent.
friends_cars = cars[:]
friends_cars.append('porsche')
cars.append('mazda')
print(cars)
print(friends_cars)

for car in cars:
    if car == 'bmw':
        print('I think that ' + car.upper() + '\'s are beautiful')
    else:
        print('I think that ' + car.title() + '\'s are beautiful')

#  make a tuple
mothafuckintuple = (200, 50, 909, 234)
for number in mothafuckintuple:
    print(number)

# rewrite a tuple
mothafuckintuple = (198, 234, 56, 123)

for number in mothafuckintuple:
    print(number)