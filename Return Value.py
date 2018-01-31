#Store answer or response to use later as a variable

# calculate age of girls allowed to date

def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

Gid_limit = allowed_dating_age(36)
print("Gid can date girls ", Gid_limit, "or older")

creepy_joe_limit = allowed_dating_age(49)
print("Creepy Joe can date girls ", creepy_joe_limit, "or older")
