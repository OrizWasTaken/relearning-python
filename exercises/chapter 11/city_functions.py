def city_country (city, country, population = ''):
    """Generate a string of the form `city, country` """
    if population:
        return f"{city.title()}, {country.title()} - population {population}."
    else:
        return f"{city.title()}, {country.title()}."