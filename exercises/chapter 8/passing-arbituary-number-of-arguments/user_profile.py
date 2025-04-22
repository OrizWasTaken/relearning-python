def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('joseph', 'orisakwe',
                                age = '19',
                                race = 'black',
                                country = 'nigeria')
print(user_profile)