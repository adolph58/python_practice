def car(brand, type, **car_info):
    car_info['brand'] = brand
    car_info['type'] = type
    return car_info

car_info = car('toyota', 'rongfang',
              color='blue',
              model='suv'
              )

print(car_info)
