class Car:
    runs = True

    def __init__(self, name):
        print(f'New car')
        self.name = name

    def start(self):
        if self.runs:
            print(f'{self.name} is started')
        else:
            print(f'{self.name} is broken!!')
