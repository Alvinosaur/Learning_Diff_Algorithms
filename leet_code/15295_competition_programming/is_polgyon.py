from math import *
from sys import stdin, stdout  

side_length = 1
DEG_TO_RAD = pi / 180


def dist(x, y):
    return sqrt(x**2 + y**2)


def is_polgyon(angle):
    angle = pi - angle  # get interior angle
    prev = (side_length * cos(angle), side_length * sin(angle))   # (x, y)
    cur_angle = angle
    found_sol = False
    while(cur_angle == angle or 
            dist(prev[0], prev[1]) > side_length):
        cur_angle += angle
        x = prev[0] + side_length * cos(cur_angle)
        y = prev[1] + side_length *  sin(cur_angle)
        prev = (x, y)
        # if distance from current to starting == side_length, found solution
        if (isclose(dist(x, y), side_length)):
            return True

    return False

# print(is_polgyon(30 * DEG_TO_RAD))
# print(is_polgyon(60 * DEG_TO_RAD))
# print(is_polgyon(90 * DEG_TO_RAD))

if __name__ == "__main__":
    n = stdin.readline() 
    # array input similar method 
    arr = [float(x) for x in stdin.readline().split()]
    for angle in arr:
        if is_polgyon(angle): print("YES")
        else: print("NO")

