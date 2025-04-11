cities = {
    'paris': {
        'country': 'france',
        'population': 2_048_472,
        'fact': "known as the 'city of light'" 
    },
    'new york': {
        'country': 'united states',
        'population': 8_260_000,
        'fact': "the most populous city in U.S"
    },
    'dubai': {
        'country': 'united arab emirates',
        'population': 3_907_733,
        'fact': "home to the world's tallest building"
    }
}

for city, info in cities.items():
    print(f"\n{city.title()} is a city in {info['country'].title()}.")
    print(f"It has a population of {info['population']}.")
    print(f"A fun fact about {city.title()} is that it's {info['fact']}.")
