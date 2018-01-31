# Use a function with a flexible amount of arguments

# Args can be named anything like tuna, or bacon

def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)

add_numbers(3)
add_numbers(2, 4)
add_numbers(3, 5, 23)

'''Out Put
3
6
31
'''
