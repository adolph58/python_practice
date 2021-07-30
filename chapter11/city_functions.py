def get_country_city(city, country, population=None):
    """返回整洁的城市国家名称"""
    if population:
        city_country = f"{city}, {country} - population {population}"
    else:
        city_country = f"{city}, {country}"
    return city_country.title()
