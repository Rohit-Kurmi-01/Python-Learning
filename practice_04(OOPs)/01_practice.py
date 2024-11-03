class Car:

    def __init__(self ,userbrand,usermodal):
        self.brand = userbrand
        self.modal = usermodal

# instance 1
my_car = Car("jaguar" , "hundai")

print(my_car.brand)
print(my_car.modal)

# instance 2
my_new_car = Car("tata" ,"Corola")
print(my_new_car.brand)
print(my_new_car.modal)