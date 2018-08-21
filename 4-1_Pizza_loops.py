pizzas = ['pepperoni', 'hawaiian', 'chicken bacon alfredo']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza.\n')

print('Yum, Yum pizza!')

squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

squares_deux = [values**2 for values in range(1, 11)]
print(squares_deux)
