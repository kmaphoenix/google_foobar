# Submitted solution

"""
Constraints:
- at most you can remove 1 wall per escape pod path
- maps start at prison exit and end at escape pod
- map is represented as matrix of 1s and 0s
- 0s are passable space
- 1s are impassable walls
- prison door is located at (0,0)
- escape pod door is at bottom right (w - 1, h - 1)

Goal:
- generate the length of the shortest path from prison door to escape pod
- you are allowed to remove 1 wall as part of your remodeling plan
- path length = total number of passable nodes (including entrance/exit nodes)
- start/end are always passable (0)
- map is always solvable, and you may not need to remove a wall
- 2 > h / w > 20
- moves in cardinal directions only

Test Cases:
Input = [
    [0,1,1,0], 
    [0,0,0,1], 
    [1,1,0,0], 
    [1,1,1,0]
    ]
Output = 7

Input = [
    [0,0,0,0,0,0],
    [1,1,1,1,1,0],
    [0,0,0,0,0,0],
    [0,1,1,1,1,1],
    [0,1,1,1,1,1],
    [0,0,0,0,0,0]]
Output = 11

Notes:
- Time complexity is O(row*col)
"""
4
import numpy as np

# recursion function to solve the maze
def solve_maze(x,y,maze):

    w = len(maze[0])
    h = len(maze)

    # Creating an N * N blank maze
    solution = [[0 for i in range(w)] for i in range(h)]
    solution[x][y] = 1

    coords = [(x,y)]

    while coords:
        x, y = coords.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
            xx, yy = x + i[0], y + i[1]
            if 0 <= xx < h and 0 <= yy < w:
                if solution[xx][yy] is 0:
                    solution[xx][yy] = solution[x][y] + 1
                    if maze[xx][yy] == 1:
                        continue
                    coords.append((xx,yy))

    return solution

def solution(maze): 

    w = len(maze[0])
    h = len(maze)

    forward = solve_maze(0, 0, maze)
    backward = solve_maze(h-1, w-1, maze)
    print(np.array(forward))
    print('\n')
    print(np.array(backward))

    # ans = 2 ** 32-1
    distance = 10000000
    for i in range(h):
        for j in range(w):
            if forward[i][j] and backward[i][j]:
                distance = min(forward[i][j] + backward[i][j] - 1, distance)
    
    return distance

if __name__ == '__main__':
    maze = [[0,1,1,0], [0,0,0,1], [1,1,0,0], [1,1,1,0]]
    # maze = [[0,0,0,0,0,0],[1,1,1,1,1,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[0,1,1,1,1,1],[0,0,0,0,0,0]]

    print(solution(maze))