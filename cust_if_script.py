#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = "Your grade is"

# wrap connection in a float() to accept decimals as numbers
score = int(input("What is your score : "))

if score >= 90 and score <= 100:
   grade = 'A'
elif score >= 80 and score < 90:
   grade = 'B'
else:
   grade = 'F'

print(message , grade)

