rivers = {'nile': 'egypt',
          'huang river': 'china',
          'chang river': 'china'
          }
for river, national in rivers.items():
    print(f"The {river} runs through {national.title()}")

for country in set(rivers.values()):
    print(country.title())
