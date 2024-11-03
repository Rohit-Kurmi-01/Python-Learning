class Car:

    def __init__(self ,userbrand,usermodal):
        self.brand = userbrand
        self.modal = usermodal

    def full_name(self):
        return f"{self.modal} {self.brand}"
    
class Electric_car(Car):
    def __init__(self, brand, modal, battery_size):
        super().__init__(brand,modal)
        self.battery_size = battery_size

my_tesla = Electric_car("Tesla", "modal S", "56KwH")
print(my_tesla.modal)

print(my_tesla.full_name())


# instance 1
my_car = Car("jaguar" , "hundai")

print(my_car.brand)
print(my_car.modal)

print(my_car.full_name())


# instance 2
my_new_car = Car("tata" ,"Corola")
print(my_new_car.brand)
print(my_new_car.modal)