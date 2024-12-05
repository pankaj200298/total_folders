class car :
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started ......")

    @staticmethod
    def stop():
        print("car stopped .......")

class toyotacar(car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name= name
        super().start()
        super().stop()


car1 = toyotacar("prius" , "hybrid")
print(car1.name)
print(car1.type)
# car1.start()
# car1.stop()