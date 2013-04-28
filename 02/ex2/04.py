# By AnnaGajdova from forums
# You are in the middle of a jungle. 
# Suddenly you see an animal coming to you. 
# Here is what you should do if the animal is:

# zebra >> "Try to ride a zebra!"
# cheetah >> If you are faster than a cheetah: "Run!" 
#            If you are not: "Stay calm and wait!". 
#            The speed of a cheetah is 115 km/h.
# anything else >> "Introduce yourself!"

# Define a procedure, jungle_animal, 
# that takes as input a string and a number, 
# an animal and your speed (in km/h), 
# and prints out what to do.

def jungle_animal(animal, my_speed):
    # YOUR CODE HERE
    text = "Introduce yourself!"
    if animal == "zebra":
        text = "Try to ride a zebra!"
    if animal == "cheetah" and my_speed <= 115:
        text = "Stay calm and wait!"
    if animal == "cheetah" and my_speed > 115:
        text = "Run!"
    print text


#jungle_animal('cheetah', 30)
#>>> "Stay calm and wait!"

#jungle_animal('gorilla', 21)
#>>> "Introduce yourself!"
