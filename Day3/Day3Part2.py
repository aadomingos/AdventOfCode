import numpy as np

with open("/Users/AADAir/GitHub/AdventOfCode/Day3/Day3.txt", "r") as f:
    treeMap = f.read().splitlines()

# this might be more efficient that a huge for-loop    
def treeCounter(listMap, slope):
    # set variables to start
    trackWidth = len(listMap[0])
    distance = len(listMap)
    right = 0
    down = 0
    trees = 0

    # the trajectory down cannot excede the distance down the mountain
    while down+1 < distance:
        # take right and down vals from slope
        right += slope[0]
        down += slope[1]
        # modulo allows the map to be "infinite"
        if listMap[down][right % trackWidth] == '#':
            trees += 1
    return trees


# new set of slope variable
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

totalCounts = []
# iterate over each set of slopes
for vals in slopes:
    treeCount = treeCounter(treeMap, vals)
    totalCounts.append(treeCount)


print("You will encounter", np.prod(totalCounts), "trees.")