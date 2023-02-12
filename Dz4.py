import random

class Human:
    def __init__(self, name="Human"):
        self.name = name
        self.revolver = Revolver()
        self.alive = True

    def game_death(self):
        if self.revolver.revolver == True:
            print('Dead')
        else:
            print('alive')

class Revolver:
    def __init__(self):
        self.revolver = list(revolver_list.values())[random.randint(0, 1)]['patron']

revolver_list = {'Rev1': {'patron': True},
                 'Rev2': {'patron': False}}

nick = Human(name='Nick')
nick.game_death()