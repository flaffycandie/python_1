# object_oriented_programming
class Cars:
    # constructor_method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

        # a_method_function
    def describe_car (self):
        print(f" My dream car is {self.make}, whose model is {self.model} from the year {self.year}")


# creating an object or instances of a class
myobj = Cars('Tesla', 'Model S', '2020')
myobj.describe_car()
myobj2=Cars('Bentley', 'Continental GT', '2021')
myobj2.describe_car()
myobj3=Cars('Mercedes', 'Benz', '2022')
myobj3.describe_car()
myobj4=Cars('BMW', 'X5', '2023')
myobj4.describe_car()