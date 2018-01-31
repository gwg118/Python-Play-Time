'''
When a variable is created outside a function, any function can access it.
If created inside a function only that function can access.
'''

a = 34
def corn():
    print(a)

def fudge():
    print(a)

corn()
fudge()
