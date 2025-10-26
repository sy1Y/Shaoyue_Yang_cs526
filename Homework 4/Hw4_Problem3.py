import sys
import math
from collections import defaultdict
from math import gcd
import time

#Define algorithm:
#Normalize the vectors
def normalize(v_x,v_y):
    if v_x == 0 and v_y == 0:
        return (0,0)
    if v_x == 0:
        return (0,1)
    if v_y == 0:
        return (1,0)
    divisor = gcd(int(v_x), int(v_y))
    v_x //= divisor #round down
    v_y //= divisor
    #Make all numbers positive
    if v_x<0 or (v_x==0 and v_y==0):
        v_x, v_y = -v_x, -v_y
    return (v_x, v_y)
#Create a perpendicular vector by rotating a vector 90 degrees
def perpendicular(V):
    (x,y) = V
    return normalize(-y, x)

def count_rightTri(points):
    n = len(points)
    total = 0
    for i in range(n):
        x1, x2 = points[i] #Traverse each point
        v_count = defaultdict(int) #Create a dictionary to count vectors
        #Simplify each vectors
        for j in range(n):
            if i == j:
                continue
            v_x = points[j][0] - x1
            v_y = points[j][1] - x2
            v_count[normalize(v_x, v_y)] += 1
            #For each vector, find the perpendicular direction
        for V, cnt in v_count.items():
            perp = perpendicular(V)
            if perp in v_count:
                total += cnt * v_count[perp]
    #since two vectors perpendicular, each right triangle is counted by twice            
    return total//2  

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    points = [tuple(map(int,line.split())) for line in lines[1:n+1]]

    start = time.time()
    answer = count_rightTri(points)
    end = time.time()

    print(f"Answer: {answer}")
    print(f"Runtime:{end - start:.3f} seconds")
    

#Program Entry
if __name__ == "__main__":
    main()
