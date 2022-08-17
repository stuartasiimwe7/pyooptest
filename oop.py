class human:
    def man(self, name, age, height):
        print("I am the Man")
        return name, age, height
        
    def woman(self, name, age, height):
        print("I am the Woman")
        return name, age, height

human1 = human()
human1.man("Stuart",25,182)
print(human1)