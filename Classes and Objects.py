# Classes and Objects
# Classes - easy way to group similar variables and functions together.

class Enemy: #name class with upper case to diff between variables and other functions
    life = 3

    def attack(self): #function to attack and enemy.
        print("OUCH!")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("I am dead!")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy() # Created enemy1 object to use stuff from class Enemy.
enemy2 = Enemy()


enemy1.attack()
enemy1.attack()
enemy1.checkLife()

enemy2.attack()
enemy2.checkLife()

'''
Output
OUCH!
OUCH!
1 life left
OUCH!
2 life left

'''
