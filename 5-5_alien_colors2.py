points = 0
while True:

    color = input('Did you kill a red, green, or yellow alien?\n')

    if color.lower() == 'green':
        points += 5
    elif color.lower() == 'yellow':
        points += 10
    elif color.lower() == 'red':
        points += 15
    else:
        print('That\'s not an option, idiot!')
    print('You currently have ' + points.__str__() + ' points!')


