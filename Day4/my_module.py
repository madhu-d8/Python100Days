# my_favourite_number = 3.1415
#above was imported

import random
friends = ["madhu" , "manoj" , "mitha" , "dudipala" , "aramareddy"]
#option1
print(random.choice(friends))
#option2
random_index = random.randint(0,4)
print(friends[random_index])
