#!/usr/bin/env python3
"""RZFeeser@alta3.com | Alta3 Research
   Using the CSV library to work with CSV data."""

# standard library import
import csv

# open our csv data (we want to loop across this)
with open("csv_users.txt", "r") as csvfile:
    # counter to create unique file names
    i = 0
    # loop across our open file line by line
    for row in csvfile:
        i = i + 1 # increase i by 1 (to create unique admin.rc file names)
        filename = f"admin.rc{i}" # this f string says "fill in the value of i"

        if  i > 2:
            break;
        print ("row is", row)
    i = 0
    for row in csv.reader(csvfile):
        i = i + 1 # increase i by 1 (to create unique admin.rc file names)
        filename = f"admin.rc{i}" # this f string says "fill in the value of i"

        if  i > 2:
            break;
        print ("row is", row)

# all of the indentation ends, so all files are auto closed

# display this to the screen when all of the looping is over
print("admin.rc files created!")

