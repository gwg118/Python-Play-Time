class Mario():
    def move(self):
        print("I am moving")

class Shroom():
    def eat_shroom(self):
        print("Now I am big!")

# class inherit from mario and Shroom
class BigMario(Mario, Shroom):
    pass # pass handles any syntax errors

bm = BigMario()
bm.move()
bm.eat_shroom()

'''
BigMario class inherits from class Mario and class Shroom to output

I am moving
Now I am big!

'''
