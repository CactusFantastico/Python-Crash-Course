fav_fruits = []
count = 1
print('List your five favorite fruits:\n')
while fav_fruits.__len__() < 5:
    fav_fruits.append(input(count.__str__() + ': ').lower())
    count += 1
print(fav_fruits)

if 'apple' in fav_fruits:
    print('Apples are awesome!')
    count += 1
if 'cantaloupe' in fav_fruits:
    print('I\'m surprised you spelled cantaloupe correctly!')
    count += 1
if 'banana' in fav_fruits:
    print('It\'s banana\'s! b a n a n a s!')
    count += 1
if 'orange' in fav_fruits:
    print('Orange you glad I didn\'t say banana?')
    count += 1
if 'tomato' in fav_fruits:
    print('Ew. Tomatoes? You\'re gross.')
    count += 1
if count < 10:
    print('I\'ve never heard of the rest...')
else:
    print('That\'s a pretty good list!')