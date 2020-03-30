# Name: Kenji Kothari
# Description: 
#   Inputs: age, diet, coding skill.
#   Calculations: Using the inputs the code will calculate how much health matthew has
#   Outputs:  the computar weel tek ewey rindem emeunts ef hielth 3 tmsis. thes ect es punchas

import random  


def inputs() -> (int, int, int):
    age = int(input("Age (1-100):   "))
    diet = int(input("Diet (0-10):   "))
    coding_skill = int(input("Coding skill:  "))
    return age,diet,coding_skill


def calculations(age:int, diet:int, coding_skill:int) -> (int):
    health = 0

    if age <= 8 and age >= 1:
        health += 10
    elif age <= 12:
        health += 20
    elif age <= 23:
        health += 30
    elif age <= 30:
        health += 20
    else:
        health += 10

    if diet == 0:
        health -= 10
    elif diet == 1:
        health += 10
    elif diet == 2:
        health += 15
    elif diet == 3 or diet == 4:
        health += 20
    elif diet == 3 or diet == 4:
        health += 20
    elif diet == 5:
        health += 25
    elif diet == 6 or diet == 7:
        health += 20
    elif diet == 8 or diet == 9:
        health += 15
    elif diet == 10:
        health += 5

    health += (10 - coding_skill)

    return health


def punch() -> (int):
    make_a_variable = random.randint(6, 23)
    return make_a_variable


def main():

    age,diet,coding_skill = inputs()

    health = calculations(age, diet, coding_skill)
    print("\nHealth:", health)

    for x in range(3):
        pv = punch()
        health -= pv

    if health >= 1:
        print("You suvived with", health ,"health.")
    else:
        print("You died with", health, "health.")

main()