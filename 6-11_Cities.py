cities = {}

#  loops for as many cities as you'd like.
while True:
    city_add = input('Please enter your city: ')
    print('Alright! Lets learn about ' + city_add.title() + '!')
    print('\n')

    #  this creates a city dictionary variable to add to the cities dictionary.
    cities[city_add.lower()] = city_dict = {}

    city_dict['population'] = int(input('What is your cities population?\n'))
    if city_dict['population'] > 600000:
        print('Wow! ' + city_add.title() + ' is a big city!')
    elif city_dict['population'] > 20000:
        print(city_add.title() + ' is a decent sized city!')
    else:
        print(city_add.title() + 'is pretty small!')
    print('\n')

    city_dict['elevation'] = int(input('What is your cities elevation in feet?\n'))
    if city_dict['elevation'] > 1000:
        print('Awesome! {} is a really high city!'.format(city_add.title()))
    elif city_dict['elevation'] > 200:
        print('Hey, that\'s not bad!')
    else:
        print('{} is pretty low!'.format(city_add.title()))
    print('\n')

    city_dict['fun fact'] = input('What is one fun fact about your city?\n')
    print('Wow, that is interesting!\n')
    print('\n')

    #  this prints the information collected from your current city
    print('Here\'s what we now know about {}!'.format(city_add.title()))
    for info, value in city_dict.items():
        print(str(info).title() + ': ' + str(value))
    print('\n')

    #  recursion
    if input('\nWould you like to enter another city?\n').lower() == 'no':
        break

#  checking to make sure I'm doing this right.
print(cities)
