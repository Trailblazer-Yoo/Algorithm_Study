import sys

input_s = lambda : sys.stdin.readline().strip()

n, m = map(int,input_s().split())
relation = [list(map(int,input_s().split())) for _ in range(m)]

print(n)
print(m)
print(relation)