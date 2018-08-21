users = {
    'maxwell': {},
    'kimberly': {},
    'zoe': {},
    }

#  user name selector that repeats till a viable username
end = False
while end is False:
    user_select = input('What is your name: ')
    if user_select.lower() in users:
        end = True
        print('Welcome ' + str(user_select.title()) + '! Lets get started!')

    else:
        print('User name not found')
#  user.select is a string and cannot be adjusted like a key in a dictionary. By selecting the specific key inside the
#  the dictionary, we can set that equal to the new variable "users_dict" and then reference it later to modify the
#  initial dictionary.

#  start adding favorite items to their dictionary.
users_dict = users[user_select.lower()]
users_dict['color'] = input('What is your favorite color:  ')
users_dict['food'] = input('What is your favorite food: ')
users_dict['birth'] = input('What is your birthday in mm/dd/yyyy form: ')
users_dict['number'] = input('What is your favorite number: ')

for key, value in users_dict.items():
    print('\nKey: ' + key)
    print('Value: ' + value)