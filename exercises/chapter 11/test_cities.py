from city_functions import city_country

def test_city_country():
    """Do names like 'Chile, Santiago.' work?"""
    formatted_city =  city_country('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile.'

def test_city_country_population():
    """Do values like chile, santiago, population=5000000 work?"""
    formatted_city =  city_country('santiago', 'chile', population=5000000)
    assert formatted_city == f'Santiago, Chile - population 5000000.'
