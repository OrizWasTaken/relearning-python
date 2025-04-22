# defining `make_shirt` with default values
def make_shirt(size='large', msg='I love Python'):
    """Summarize the shirt I'm going to make."""
    print(f'I\'m making a {size} t-shirt that\'ll say, "{msg}".')

# making shirts of differnt sizes
make_shirt('meduim')
make_shirt(size='large')

# making a shirt with an 'I love Jesus' message
make_shirt('small', msg='I love Jesus')