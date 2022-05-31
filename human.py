import contextlib
from player import Player

class Human(Player):
    def __init__(self,name):
        super().__init__(name)
    
    def choose_name(self):
        self.name = input('Please enter your name? ')
        print(f'Welcome {self.name}')
    
    def choose_gesture(self):
        for l in range(len(self.list_of_gesture)):
            if l == 0:
                l = 1
            else:
                print(l, self.list_of_gesture[l])
        self.human_choice_input = input(f'pick one: ')
        print(f'you chose {self.list_of_gesture[int(self.human_choice_input)]}')
        self.picked_gesture = self.list_of_gesture[int(self.human_choice_input)]
        
