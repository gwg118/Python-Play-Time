def health_calculator(age, apples_ate, cig_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (cig_smoked * 2)
    print (answer)

gids_data = [36,10, 0]

health_calculator(gids_data[0], gids_data[1], gids_data[2])

#Unpacking argument list - takes list and pass each item in one at a time.

health_calculator(*gids_data)
