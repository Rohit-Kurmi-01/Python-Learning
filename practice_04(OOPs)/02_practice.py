class Car:
    total_car = 0


    def __init__(self ,userbrand,usermodal):
        self.__brand = userbrand
        self.modal = usermodal
        Car.total_car += 1 
    
    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.modal} {self.brand}"
    
    def fuel_type(self):
        return " car"
    @staticmethod #decorator
    def general_desc(self):
        return "Cars are means of transport"
    
class Electric_car(Car):
    def __init__(self, brand, modal, battery_size):
        super().__init__(brand,modal)
        self.battery_size = battery_size
    def fuel_type(self):
        return "electric car"
    
safari = Car("tata", "Safari")
print(safari.fuel_type())

my_car1 = Car("tata", "Safari")
# print(my_car1.general_desc())

my_tesla = Electric_car("Tesla", "modal S", "56KwH")
print(my_tesla.fuel_type())

# print(my_tesla.full_name())


# instance 1
my_car = Car("jaguar" , "hundai")

print(my_car.get_brand())
# print(my_car.modal)

print(Car.total_car)
# print(my_car.full_name())


# # instance 2
# my_new_car = Car("tata" ,"Corola")
# print(my_new_car.brand)
# print(my_new_car.modal)