#!/usr/bin/env python3
## create file object in "r"ead mode
file = input("Enter file name\n")
with open(file, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

    print(len(configlist))

