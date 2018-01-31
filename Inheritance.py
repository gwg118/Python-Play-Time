class Parent():

    def print_last_name(self):
        print("Gordon")

class Child(Parent): # Child class can inherit from parent class

    def print_first_name(self):
        print("Gideon")

    #Over wtite Parient class print_last_name
    def print_last_name(self):
        print("Persaud")



brother = Child()

brother.print_first_name()
brother.print_last_name()


