# Bismillah
"""
Created on Fri Aug 23 18:20:14 2024

@author: Faxriddin
"""

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
def info_100():
    name = input("What is your name: ")
    age = int(input("How old are you now: "))
    b_day = input("Are you already celebrate your birthday in this year? (yes/no) \n>>>")
    if b_day == 'yes':
        years = 100 - age
    else:
        years = 99 - age
    
    
    return f"Dear {name.title()} you will turn 100 years old after {years} years in {2024 + years}"

print(info_100())