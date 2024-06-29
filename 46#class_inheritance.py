class Animal :
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale.Exhale")
    
class Fish(Animal):
    def __init__(self):
        super().__init__
    def breathe(self):
        super().breathe()
        print("Do this under water")
    def swim(self):
        print("moving on the water")

fish = Fish()
fish.breathe()




