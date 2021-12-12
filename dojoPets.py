class Ninja():
    def __init__(self, first_name, last_name, pet, pet_food, treats):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.pet_food = pet_food
        self.treats = treats

    def walk(self, Pet):
        Pet.play()
        return self

    def feed(self, Pet):
        Pet.eat()
        return self

    def bathe(self, Pet):
        print("It's bath time!!")
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
        print(f"{self.name} looks excited to go for a walk, its health is now {self.health}")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} is now fed! Its health is now {self.health} and its energy is {self.energy}")
        return self

    def noise(self):
        print("ANGRY ANIMAL NOISE!")
        print(f"{self.name} looks very upset!!")
        return self

    def sleep(self):
        self.energy += 25
        print("ZzZzzZzzzZzzzz")
        print(f"{self.name}'s energy is now {self.energy}")
        return self

John = Ninja("John", "Williams", "Dog", "dog_food", "dog_treats")
Doggo = Pet("Doggo", "dog", "none", 90, 80)

John.feed(Doggo).walk(Doggo).bathe(Doggo)