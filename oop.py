class human:
    def __init__(self, name, age, height) -> None:
        self.name = name
        self.age = age
        self.height = height
        print(name,age,height)

    def man(self):
        print("I am the Man")
         
    def woman(self):
        print("I am the Woman")

human1 = human("Stuart",25,182)
#human1.man("Stuart",25,182)
#print(human1)