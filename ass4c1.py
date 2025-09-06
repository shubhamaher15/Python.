#Write a program to illustrate function duck typing. 
class Duck:
    def sound(self):
        print("Quack Quack!")

class Dog:
    def sound(self):
        print("Bark Bark!")
def make_sound(animal):
    animal.sound()   

duck = Duck()
dog = Dog()

make_sound(duck)   
make_sound(dog)   
