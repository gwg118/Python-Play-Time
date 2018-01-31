# To help exception errors(user error)
while True:
    try:
        number = int(input("What is your favorite number?\n "))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number")
    except ZeroDivisionError:
        print("Function can not be devided by 0 ")

# Finally runs every time

    finally:
        print("Go home, your drunk!" )


'''
OutPut
What is your favorite number?
 dfe
Make sure and enter a number
Go home, your drunk!
What is your favorite number?
 0
Function can not be devided by 0 
Go home, your drunk!
What is your favorite number?
 8
2.25
Go home, your drunk!
'''
