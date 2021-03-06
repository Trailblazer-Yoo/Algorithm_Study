import sys

input_s = lambda : sys.stdin.readline().strip()

n = int(input_s())
s = input_s()

# i = 0
# R이면 +1, L이면 -1
# direction = ["s","w","n","e"]

def change_direction(d,r):
    if r == "R":
        d += 1
    else:
        d -= 1
    curr_d = d % 4
    return curr_d

def move_forward(d,curr):
    global all_i
    global all_j
    global all_c
    if d == 0:
        next = [curr[0]+1,curr[1]]
    elif d == 1:
        next = [curr[0],curr[1]-1]
    elif d == 2:
        next = [curr[0]-1,curr[1]]
    elif d == 3:
        next = [curr[0],curr[1]+1]
    if next not in all_c:
        all_c.append(next)
        all_i.append(next[0])
        all_j.append(next[1])
    return next

direction = 0
curr = [0,0]
all_i = [0]
all_j = [0]
all_c = [[0,0]]

for action in s:
    if action == "R" or action == "L":
        direction = change_direction(direction,action)
    else:
        curr = move_forward(direction,curr)

for i in range(len(all_i)):
    all_c[i][0] += -min(all_i)
    all_c[i][1] += -min(all_j)

maze = [["#"] * (max(all_j)-min(all_j)+1) for i in range(max(all_i)-min(all_i)+1)]

for coo in all_c:
    maze[coo[0]][coo[1]] = "."

for i in range(len(maze)):
    for j in range(len(maze[0])):
        print(maze[i][j],end="")
    print()
