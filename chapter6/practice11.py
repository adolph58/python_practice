cities = {
    'Guangzhou': {'country': 'China', 'population': '20000000', 'fact': 'Yayunhui'},
    'New York': {'country': 'US', 'population': '2500000', 'fact': '911'},
    'Tokoy': {'country': 'Janpan', 'population': '18000000', 'fact': 'hot'},
    }

for city, infos in cities.items():
    print(f"City: {city}")
    for key, value in infos.items():
        print(f"{key}----->{value}")
