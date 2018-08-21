def greet_user(name):
    """Display a simple greeting."""
    print('Hello, {}!'.format(name.title()))


name = input('What is your name?\n')
greet_user(name)
