# Collections of items with no dupliates unlike a list.

groceries = {'cereal', 'cheese', 'milk', 'bacon', 'beef', 'beer', 'chicken', 'toilet paper', 'beer', }

print(groceries)

'''Out Put
Notice beer only print once

{'beer', 'bacon', 'cheese', 'toilet paper', 'cereal', 'milk', 'beef', 'chicken'}
'''

if 'milk' in groceries:
    print("You already have milk!")
else:
    print("Item is not on list.")

