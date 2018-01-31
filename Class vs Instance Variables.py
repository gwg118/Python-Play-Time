# Class variable - any object created from a class will have the default class variables example gender female
# Instance variable - each object instance will have its own variable. Unique to each object example name

class Girl:

    #class variable
    gender = "female"

    #instance variable
    def __init__(self, name):
        self.name = name #variable name and set it to whatever name we pass in

r = Girl('Sally')
s = Girl('Jen')
print(r.gender)
print(s.gender)
