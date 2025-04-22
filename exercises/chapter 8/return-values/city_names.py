def city_country(city, country):
    """Return a string formatted like 'Santiago, Chile'."""
    return f'{city.title()}, {country.title()}'

city = city_country('lagos', 'nigeria')
print(city)

city = city_country(city='abuja', country='nigeria')
print(city)

city = city_country(country='france', city='paris')
print(city)