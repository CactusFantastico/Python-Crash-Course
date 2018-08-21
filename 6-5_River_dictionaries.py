#  define dictionary
rivers = {'nile': 'egypt', 'colorado': 'california', 'seine': 'paris'}
req_rivers = ['mississippi', 'american', 'thanes', 'nile', 'seine', 'colorado']

#  print statements regarding dictionary
for river, location in rivers.items():
    print('The ' + river.title() + ' river runs through ' + location.title() + '.')
print('\n')
for river in req_rivers:
    if river not in rivers:
        print('We still need information on the ' + river.title() + ' river.')

print('\nThese are the rivers:')
for river in rivers:
    print(river.title() + ' River')

print('\nThese are the locations:')
for location in rivers.values():
    print(location.title())

