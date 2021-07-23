class Restaurant:
    """这是一家餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性 restaurant_name 和 cuisine_type """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """餐厅简介"""
        print(f"The restaurant's name is {self.restaurant_name}.")
        print(f"It's a {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """餐馆营业状态"""
        print("The restaurant is opening")

sichuan_restaurant = Restaurant('Dalongyi', 'Sichuan')
sichuan_restaurant.describe_restaurant()
hunan_restaurant = Restaurant('Laochangsha', 'Hunan')
hunan_restaurant.describe_restaurant()
guangdong_restaurant = Restaurant('Bingsheng', 'Guangdong')
guangdong_restaurant.describe_restaurant()
