def get_city_population(populations, city):
    try:
        return populations[city]
    except KeyError:
        raise KeyError(f'City "{city}" not found in population data.')