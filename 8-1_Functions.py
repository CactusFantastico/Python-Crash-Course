def greet_user(name):
    """Display a simple greeting."""
    print('Hello, {}!'.format(name.title()))


name = input('What is your name?\n')
greet_user(name)


def shirt_maker(size, color, front_mess, back_mess, back=False):

    """Describes the shirt being made. Color, size, and writing on front and/or back."""
    if back is False:
        print('You\'ve ordered a {} {} shirt with {} written on the front.'.format(size, color, front_mess))
    else:
        print('You\'ve ordered a {} {} shirt with {} written on the front,'
              ' and {} written on the back.'.format(size, color, front_mess, back_mess))


while True:
    print('\nLets make a shirt!\n')
    shirt_size = input('What size shirt would you like? ')
    shirt_color = input('\n what color shirt would you like? ')
    back_option = input('\nWould you like text on both sides or just the front? ')
    front_message = input('\nwhat would you like the front to say? ')
    if 'both' in back_option:
        back_message = input('\nWhat would you like the back to say? ')
        back_option = True
    else:
        back_message = ''
        back_option = False
    print('Perfect! Lets see what we have.')
    shirt_maker(size=shirt_size, color=shirt_color,
                front_mess=front_message, back_mess=back_message, back=back_option)
    correct = input('Is this correct? ').lower()
    if 'no' in correct:
        print('Lets start over then, shall we?')
        continue
    repeat = input('Shall we make another? ').lower()
    if 'no' in repeat:
            break
