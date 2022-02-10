class Ninja:

    # implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__(self, first_name, last_name, treats, pet_food,pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet


        # implement the following methods:
        # # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print("calling play method from pet class...")
        self.pet.play()
        self.pet.display()
        return self

        # # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print("calling eat method from pet class...")
        self.pet.eat()
        self.pet.display()
        return self

        # # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print("calling bathe method from pet class...")
        self.pet.noise()
        return self


class Pet:

    # implement __init__( name , type , tricks ):
    def __init__( self, name , type , tricks ):
        self.name = name
        self.type = type
        self.tricks =tricks
        self.energy = 100
        self.health = 100

    # implement the following methods:
    # sleep() - increases the pets energy by 25
    def sleep(self):
        print("sleepping...")
        self.energy  += 25
        return self
    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        print("eating...")
        self.energy  += 5
        self.health  += 10
        return self
    # play() - increases the pet's health by 5
    def play(self):
        print("playing...")
        self.health += 5
        return self
    # noise() - prints out the pet's sound
    def noise(self):
        print("doodle doo doo...")


    def display(self):
        print(f'Name: {self.name}, type: {self.type}, tricks: {self.tricks}, Energy: {self.energy}, Health: {self.health}')
        return self

class Dog(Pet):
    def barking(self):
        print("Woof, woof, woff...")

if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)


