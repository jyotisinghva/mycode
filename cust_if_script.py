#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = "Your grade is"

# wrap score in a int() to accept numbers
score = int(input("What is your score : "))

if score >= 90 and score <= 100:
   grade = 'A'
elif score >= 80:
   grade = 'B'
elif score >= 70: 
   grade = 'C'
elif score >= 60:
   grade = 'D'
else:
   grade = 'F'

print(f"Your grade is {grade}")

