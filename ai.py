from player import Player
import random

class AI(Player):
    def __init__(self, name):
        super().__init__(name)

    def choose_name(self):
        self.name = 'AI'

    def choose_gesture(self):
        self.random_choice = random.randint(1,5)
        print(f'AI has chosen {self.list_of_gesture[self.random_choice]}')
        self.picked_gesture = str(self.list_of_gesture[self.random_choice])
        return
    
