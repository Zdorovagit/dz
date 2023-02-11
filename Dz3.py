import random


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, Hobby=None):
        self.name = name
        self.job = job
        self.hobby = Hobby
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()

    def get_hobby(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.hobby = Hobby(hobby_list)
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def get_car(self):
        self.car = Auto(brand_of_car)

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety > 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def hobby(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
            return
        self.money -= self.hobby.lesion
        self.gladness += self.hobby.gladness_full
        self.satiety -= self.hobby.hunger
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
            return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 5

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == 'fuel':
            print('I bought fuel')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'food':
            print('I bought some food')
            self.money -= 50
            self.home.food += 50
        elif manage == 'delicacies':
            print('I bought some food')
        self.money -= 15
        self.satiety += 2
        self.gladness += 5

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 3
        self.home.mess -= 10

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f'Today is {day} of {self.name} is Life'
        print(f'{day:+^50}', '\n')
        human_indexes = self.name + 'is indexes'
        print(f'Money - {self.money}')
        print(f'Satiety - {self.satiety}')
        print(f'Gladness - {self.gladness}')
        home_indexes = 'Home indexes'
        print(f'{home_indexes:+^50}', '\n')
        print(f'Food - {self.home.food}')
        print(f'Mess - {self.home.mess}')
        car_indexes = '{0} Car indexes'.format(self.car.brand)
        print(f'{car_indexes:+^50}', '\n')
        print(f'Brand - {self.car.brand}')
        print(f'Strength - {self.car.strength}')
        print(f'Fuel - {self.car.fuel}')
        print(f'Comsuption - {self.car.comsuption}')

    def is_alive(self):
        if self.gladness <= 0:
            print('Dead Inside')
            return False
        if self.satiety <= 0:
            print("Golodomor")
            return False
        if self.money <= -200:
            print('Bankrot')
            return False

    def live(self, day):
        if self.is_alive == False:
            pass
        if self.home is None:
            print('Settled in the house')
            self.get_home()
        if self.car is None:
            print('Settled the car')
            self.get_car()
        if self.job is None:
            print('Get Job')
            self.get_job()
            print(f"I don`t have a job, I`m going to get a job {self.job.job} with salary {self.job.salary}")
        if self.hobby is None:
            print('I want hobby Dangeon Master')
            self.get_hobby()
            print(f"I don`t have a hobby, I`m going to get a hobby {self.hobby.hobby} with gladness {self.hobby.gladness_full}")
        self.days_indexes(day)
        dise = random.randint(1, 5)
        if self.satiety < 20:
            print('I gonna eat')
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 20:
                print(' I wanna chill, but there is clear')
                self.clean_home()
            else:
                print('I gonna kill you, DIOOOO')
                self.chill()
        elif self.car.strength < 15:
            print('Repair my car')
            self.to_repair()
        elif dise == 1:
            print('Chill')
            self.chill()
        elif dise == 2:
            print('WORK')
            self.work()
        elif dise == 3:
            print('CLEAN')
            self.clean_home()
        elif dise == 4:
            print('SHOPOGOLIK')
            self.shopping(manage='delicacies')
        elif dise == 5:
            print('BOY NEXT DOOR, COME TO ME AND PLAY UNTIL WE DIED')
            self.get_hobby()


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.comsuption = brand_list[self.brand]['comsuption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.comsuption:
            self.strength -= 1
            self.fuel -= self.comsuption
            return True
        else:
            print('The car cannot move')
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

class Hobby:
    def __init__(self, hobby_list):
        self.hobby = random.choice(list(hobby_list))
        self.gladness_full = hobby_list[self.hobby]['gladness_full']
        self.lesion = hobby_list[self.hobby]['lesion']
        self.hunger = hobby_list[self.hobby]['hunger']

hobby_list = {'Draw': {'gladness_full': 10, 'lesion': 50, "hunger": 5},
              'Football': {'gladness_full': 3, 'lesion': 25, "hunger": 10},
              'Tic_tac_Toe': {'gladness_full': 5, 'lesion': 5, "hunger": 6},
              'Chess': {'gladness_full': 8, 'lesion': 13, "hunger": 3},}

job_list = {'Java_develop': {'salary': 50, 'gladness_less': 10},
            'C++_develop': {'salary': 40, 'gladness_less': 3},
            'Python_develop': {'salary': 70, 'gladness_less': 8},
            'Php_develop': {'salary': 35, 'gladness_less': 5}}

brand_of_car = {'BMW': {'fuel': 100, 'strength': 100, 'comsuption': 12},
                'AUDI': {'fuel': 60, 'strength': 60, 'comsuption': 10},
                'FERARI': {'fuel': 80, 'strength': 75, 'comsuption': 11},
                'volvo': {'fuel': 50, 'strength': 80, 'comsuption': 15}}

nick = Human(name='Nick')
for day in range(1, 8):
    if nick.live(day) == False:
        break