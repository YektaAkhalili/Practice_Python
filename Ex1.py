"""
This code tells in what year you'll be 100 years old. 
"""
import datetime

now = datetime.datetime.now()
yr = now.year

name = input("Enter name: ")
age = int(input("Enter age: "))

def Turn100(num):
    year_born = yr - num 
    return (year_born + 100)

print("\nHey there, " + name.title() + ".")
print("You'll be 100 in the year " + str(Turn100(age)) + ".")