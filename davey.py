# creating a class

class Dog:
    def __init__(self, name, color, fur_length):
        self.name = name
        self.color = color
        self.fur_length = fur_length

    def print_name(self):
        print(f'Name: {self.name}')


    def print_fur_type(self):
        print(f'{self.name} has {self.color} {self.fur_length} fur')

teddy = Dog(
    name='Ted butt',
    color='ivory',
    fur_length='short'
)


ruby = Dog(
    name='Rooster',
    color='brown and white',
    fur_length='longth'
)

dogs = [teddy, ruby]
for doggo in dogs:
    print(doggo.print_fur_type())