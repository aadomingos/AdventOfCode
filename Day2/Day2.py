"""This is the Advent of Code Day 2 challenge."""

with open("/Users/AADAir/GitHub/AdventOfCode/Day2/Day2.txt", "r") as f:
    passwordList = f.read().splitlines()

data = [password.split(":") for password in passwordList]
print(data)