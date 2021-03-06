"""This is the Advent of Code Day 2 challenge."""

with open("/Users/AADAir/GitHub/AdventOfCode/Day2/Day2.txt", "r") as f:
    passwordList = f.read().splitlines()

def policy_checker(strings, letter, minFreq, maxFreq):
    freq = strings.count(letter)
    if int(minFreq) <= int(freq) <= int(maxFreq):
        return True
    else:
        return False

def entry_splitter(entry, firstSplitter, secondSplitter, thirdSplitter):
    splitEntry = entry.split(firstSplitter)
    passwrd = splitEntry[1]

    policy = splitEntry[0].split(secondSplitter)
    lettr = policy[1]

    freqRange = policy[0].split(thirdSplitter)
    minFrq = freqRange[0]
    maxFrq = freqRange[1]

    return passwrd, lettr, minFrq, maxFrq 

i = 0
for password in passwordList:
    p, l, minF, maxF = entry_splitter(password, ":", " ", "-")
    result = policy_checker(p, l, minF, maxF)
    if result is True:
        i+=1
    else:
        pass

print(i)