import os

def check_int(input_str):
    answer =input(input_str)
    try:
        answer =int(answer)
        return answer
    except:
        return None

def calculate_dose(factor, weight, level):
    '''
    Description:
    calculates the factor viii or factor ix dose you need.

    Input:
    factor: either factor viii or factor ix. 4.4 for factor viii and 2.2 for factor ix
    weight: the person's weight
    level: the factor level that should be reached after taking the dose
    '''
    return "You need a dose of {} to reach a blood factor of {}%".format(int(weight/factor*level), level)

while(True):
    print("Welcome to the Hemophilia factor dosage calculator.\nFor more information about the tool, please check the README file.")
    factor =check_int("Which blood factor are you looking for?\n1 for factor viii.\n 2 for Factor ix")
    if factor ==1:
        factor =4.4
    elif factor ==2:
        factor =2.2
    else:
        continue
    weight =check_int("Please enter your weight")
    if weight is None:
        continue
    confirm =input("Was that in Kilograms? Press y for yes, or press enter if it's in lbs")
    if confirm.lower() =="y":
        weight =weight*2.205
    level =check_int("Enter the factor level you want to reach.\nFor example:\nIf you want a clotting factor of 50%, you'd type 50")
    if level is None:
        continue
    print(calculate_dose(factor, weight, level))
    result =input("Do you want to do another calculation? y for yes, anything else to quit")
    if result.lower() !="y":
        break