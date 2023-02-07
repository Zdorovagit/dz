import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.tired = 25
        self.hungry = 10
        self.walk = 3
        self.dirty = 0
        self.alive = True

    def to_walk(self):
        print('Myau Myau Ya Hochu gulyat')
        self.gladness += 10
        self.tired += 10
        self.hungry += 5
        self.walk += 5
        self.dirty += 1

    def to_eat(self):
        print('Myau Myau jrat')
        self.hungry -= 15
        self.gladness += 5
        self.dirty += 1
        self.walk -= 0.5

    def to_wash(self):
        print('Pomoi Menya')
        self.gladness -= 20
        self.dirty -= 3
        self.walk -= 0.5

    def to_sleep(self):
        print('Hey Kojaniy Ya Spat Budu')
        self.tired -= 10
        self.gladness += 10
        self.hungry += 5
        self.walk -= 1

    def to_chill(self):
        print('Pomasiruy mne pyatki')
        self.gladness += 5
        self.tired -= 15
        self.walk -= 0.5
        self.hungry += 5

    def is_alive(self):
        if self.gladness < 10:
            self.alive = False
            print('Depression')
        elif self.dirty > 5:
            self.alive = False
            print('Gryaz s_ela kotika')
        elif self.hungry > 50:
            print('Pomer S Goloduhi')
            self.alive = False
        elif self.tired > 50:
            print('Pererabotal')
            self.alive = False
        elif self.walk < -1:
            print('Byl Razorvan Energiey')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness = {self.gladness}')
        print(f'Dirty =  {self.dirty}')
        print(f'Tired = {self.tired}')
        print(f'Hungry = {self.hungry}')
        print(f'Walk = {self.walk}')

    def live(self, day):
        day = 'Day' + str(day) + 'of' + self.name + 'life'
        print(f"{day:=^50}")
        live_cube = random.randint(1, 5)
        if live_cube == 1:
            self.to_walk()
        elif live_cube == 2:
            self.to_eat()
        elif live_cube == 3:
            self.to_wash()
        elif live_cube == 4:
            self.to_sleep()
        elif live_cube == 5:
            self.to_chill()
        self.end_of_day()
        self.is_alive()


JoJo = Cat(name='JoJo')
for day in range(365):
    if JoJo.alive == False:
        break
    JoJo.live(day)