class Pet:
# implement __init__( name , type , tricks ):
    def __init__( self, name , type , tricks ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
        pass

# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f'Sleeping, Energy level: {self.energy}')
        return(self)

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f'Eating, Energy level: {self.energy}, Health level: {self.health}')
        return(self)

# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f'Playing, Health level: {self.health}')
        return(self)

# noise() - prints out the pet's sound
    def noise(self):
        print(f'Bark I needed a bath')
        return(self)

dog = Pet('Buddy', 'Boxer', 'Stay')
