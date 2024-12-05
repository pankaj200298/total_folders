class animal:
    def __init__(self, zoo):
        self.zoo = zoo
        print(zoo)

    def zoo_capacity(self):
        print(" zoo_capacity ..... =  30  ")

    def all_animal(self):
        print( self.zoo )
        print(self.zoo_capacity())


class fruit:
    def __init__(self, fruits):
        self.fruits = fruits
        print(fruits)

    def bucket_capacity_for_fruit(self):
        print(" printing bucket  capacity =- 40 ")
    def all_fruits(self):
         print(self.fruits)
         print(self.bucket_capacity_for_fruit())

animals = {"tiger": 5, "lion": 10, "bhediya": 15}

my_animal = animal(animals)
# my_animal.zoo_capacity()
my_animal.all_animal()

my_fruit = fruit("banana")
# my_fruit.bucket_capacity_for_fruit()
my_fruit.all_fruits()
