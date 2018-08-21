usernames = ['maxwell', 'kimberly' , 'jeff', 'erik', 'troy']

#  two variables to create an exit strategy.
starting_count = usernames.__len__()

while usernames.__len__() == starting_count:

    new_user = input('Please enter a new username: ').lower()

    if new_user in usernames:
        print('That username is already taken!')
    else:
        print('New username added, ' + new_user.title() + '!')
        usernames.append(new_user.lower())
