class Enemy:
    def __init__(self, x): # init special function gets called when creating an object automatically.
        self.energy = x

    def get_energy(self):
        print(self.energy)

SubZero = Enemy(18)
Scorpion = Enemy(20)

SubZero.get_energy()
Scorpion.get_energy()


'''
Output
18
20
'''
