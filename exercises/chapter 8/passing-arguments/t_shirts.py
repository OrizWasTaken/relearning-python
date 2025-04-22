def make_shirt(msg, size):
    """Summarize the shirt I'm going to make."""
    print(f'I\'m making a {size} t-shirt that\'ll say, "{msg}".')

# calling `make_shirt` with positional arguments
make_shirt('I love Python.', 'meduim')

# calling `make_shirt` with keyword arguments
make_shirt(size='large', msg='Hello World!')
