# create a class called fruits, that has the following attibutes: name, color and price. Implement a constructor method, a method function that prints name, color and price. Create 5 instances of that class
class Fruits:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def describe_fruit(self):
        print(f'My favourite fruit is {self.name}, its color is {self.color} and its price is {self.price}')
frut1=Fruits('Apple','Red','Ksh 100')
frut1.describe_fruit()
frut2=Fruits('Banana','Yellow','Ksh 50')
frut2.describe_fruit()
frut3=Fruits('Mango','Yellow','Ksh 30')
frut3.describe_fruit()
frut4=Fruits('Pineapple','Yellow','Ksh 150')
frut4.describe_fruit()
frut5=Fruits('Watermelon','Green','Ksh 200')
frut5.describe_fruit()