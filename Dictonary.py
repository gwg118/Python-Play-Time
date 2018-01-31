'''
Dictonary- words with definitions
In Python - keys with values
'''

classmates = {'Tony': ' Cool but smells', 'Bob': ' Looks like Tony', 'John': ' always hungry'}

print(classmates)
'''{'Tony': 'Cool but smells', 'Bob': 'Looks like Tony', 'John': 'always hungry'}'''

print(classmates['Bob'])
'''Looks like Tony'''

for k, v in classmates.items():
    print(k+v)
'''
Tony Cool but smells
Bob Looks like Tony
John always hungry
'''
