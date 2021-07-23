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

class IceCreamStand(Restaurant):
    """冰激凌小店"""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        """调用父类初始化方法，并初始化特有方法"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_ice_cream(self):
        """显示冰淇淋"""
        for flavor in self.flavors:
            print(f"{flavor} ice cream")

restaurant = Restaurant('Dalongyi', 'Sichuan')
restaurant.describe_restaurant()
restaurant.open_restaurant()

ice_cream_stand = IceCreamStand('m', 'west', ['blueberry', 'apple', 'orange'])
ice_cream_stand.display_ice_cream()
