from math import inf

def fun(x1, y1, x2, y2, x3, y3, x4, y4):

    if (x2-x1 == 0):
        p = inf
    else:
        p = (y2-y1)/(x2-x1)

    if (x4-x3 == 0):
        q = inf
    else:
        q = (y4-y3)/(x4-x3)

    if(p != q):
        return True

    return False

k = 1e9+7
n = int(input())
a = []

for i in range(n):
    a.append([int(j) for j in input().split()])

c = 0

for i in range(n):
    for j in range(i+1,n):
        if(fun(a[i][0], a[i][2], a[i][1], a[i][3], a[j][0], a[j][2], a[j][1], a[j][3])):
            c+=1

print(int(c%k))