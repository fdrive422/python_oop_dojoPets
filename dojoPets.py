class Ninja():
    def __init__(self, firstName, lastName, pet, petFood, treats):
        self.firstName = firstName
        self.lastName = lastName
        self.pet = pet
        self.petFood = petFood
        self.treats = treats

    def walk(self, Pet):
        Pet.play()
        return self

    def feed(self, Pet):
        Pet.eat()
        return self

    def bathe(self, Pet):
        print("Time for a bath!")
        Pet.noise()
        return self

class Pet():
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def play(self):
        self.health += 5
        print(f"{self.name} looks excited to play, her health is now {self.health}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is fed! Her health is {self.health} and her energy is {self.energy}")
        return self

    def noise(self):
        print("Excited, barking dog!")
        print(f"{self.name} she is upset!")
        return self

    def sleep(self):
        self.energy += 25
        print(f"{self.name}'s energy is now {self.energy}")
        return self

Francis = Ninja("Francis", "John", "Dog", "dog_food", "dog_treats")
Riley = Pet("Riley", "dog", "none", 90, 80)

Francis.feed(Riley).walk(Riley).bathe(Riley)