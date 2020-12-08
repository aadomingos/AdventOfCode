"""This is the Advent of Code Day 1 challenge."""

import itertools

# Read file into a list of integers
with open("/Users/AADAir/GitHub/AdventOfCode//Day1/Day1.txt", "r") as f:
    numberList = [int(number) for number in f]

# Use itertools to get all the unique two digit combinations in the list
for combo in itertools.combinations(numberList, 2):
    # Sum the unique tuple
    winners = sum(list(combo))
    # If tuple equals the 2020, multiply the elements for the answer, if not, pass
    if winners == 2020:
        print(combo[0]* combo[1])
    else:
        pass