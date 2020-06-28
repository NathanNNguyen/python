class Vehicle:

    def __init__(self, make, model, fuel='gas'):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f'I drive {self.make} {self.model}. It runs on {self.fuel}.'


class Car(Vehicle):

    number_of_wheels = 4


class Truck(Vehicle):

    number_of_wheels = 6

    def __init__(self, make, model, fuel='diesel'):
        super().__init__(make, model, fuel)


daily = Vehicle('Huyndai', 'Sonata')
print(daily)

# daily.number_of_wheels = 3

# print('for Class', Vehicle.number_of_wheels)
# print('for this instance (daily)', daily.number_of_wheels)


class GitHubRepo:

    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars

    def __str__(self):
        return f'-> {self.name} is a {self.language} repo with {self.num_stars} stars'


vue = GitHubRepo(name='Vue', language='JavaScript', num_stars=50000)
print(vue)
