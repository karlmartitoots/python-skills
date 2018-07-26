import os

def nextCube(cubes):
    left = int(cubes[0])
    right = int(cubes[-1])
    if left > right:
        return left, cubes[1:]
    elif right > left:
        return right, cubes[:-1]
    else: 
        return left, cubes[1:]

def stackable(cubes):
    noBottom = True
    while cubes:
        left = int(cubes[0])
        right = int(cubes[-1])
        if noBottom:
            bottom = (left if left>right else right)
            noBottom = False 
        if bottom < left or bottom < right:
            return False
        else:
            bottom, cubes = nextCube(cubes)
    return True

lines = open(r'C:\Users\Karlm\Documents\PythonSkills\hackerrank\testcase2',"r")

# amountOfTests = int(input())
# for i in range(amountOfTests):
#     input()
#     if stackable(input().split(" "),10**30):
#         print("Yes")
#     else:
#         print("No")


amountOfTests = int(lines.readline())
for i in range(amountOfTests):
    lines.readline()
    if stackable(lines.readline().split(" ")):
        print("Yes")
    else:
        print("No")