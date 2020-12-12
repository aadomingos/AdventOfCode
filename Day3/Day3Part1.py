with open("/Users/AADAir/GitHub/AdventOfCode/Day3/Day3.txt", "r") as f:
    treeMap = f.read().splitlines()

# set variables to start
right = 0
down = 0
tree = 0
trackWidth = len(treeMap[0])
distance = len(treeMap)

# the trajectory down cannot excede the distance down the mountain
while down+1 < distance:
    right += 3
    down += 1
    
    # modulo allows the map to be "infinite"
    if treeMap[down][right % trackWidth] == '#':
        tree += 1

print("You will encounter", tree, "trees.")