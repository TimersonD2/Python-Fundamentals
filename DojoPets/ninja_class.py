import pet_class
# from .pet_class import Pet

class Ninja():
# implement __init__( first_name , last_name , treats , pet_food , pet )
    def __init__( self, first_name , last_name , treats , pet_food , pet ):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
        pass
    
# implement the following methods:
# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f'Walking my pet {self.pet.name}')
        self.pet.play()
        return(self)
        

# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f'Feeding my pet {self.pet.name} {self.treats}')
        self.pet.eat()
        return(self)

# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f'Bathing my pet {self.pet.name}')
        self.pet.noise()
        return(self)

dog = pet_class.Pet('Buddy', 'Boxer', 'Rollover')
eddie = Ninja('Eddie', 'Dojo', 'Bacon', 'Homemade', dog)
eddie.feed() .walk() .feed() .walk() .bathe()

