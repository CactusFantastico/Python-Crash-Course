cars = ['honda', 'toyota', 'porsche', 'audi', 'BMW']
print('My first car was a ' + cars[1])
print('My wife\'s first car was a ' + cars[0])
print('My dad\'s current car is a ' + cars[3])
cars[3] = 'tesla'
print(cars)
cars.insert(0, 'mazda')
print(cars)
cars.append('range rover')
print(cars)
popped_cars = cars.pop(0)
print(cars)
print(popped_cars)