from math import inf

def fun(x1, y1, x2, y2):

    if (x2-x1 == 0):
        p = inf
    else:
        p = (y2-y1)/(x2-x1)

    return p

k = 1e9+7

def main(a):

	# n = int(input())
	# a = []

	# for i in range(n):
	# 	a.append([int(j) for j in input().split()])
	d = {}
	c = 0

	for i in range(len(a)):
		m = fun(a[i][0], a[i][2], a[i][1], a[i][3])
		if(m in d):
			d[m]+=1
		else:
			d[m] = 1

	s = list(d.values())

	if(len(s)==1):
	    return 0
	else:
	    res = 0
	    tot = sum(s)
	    for i in range(len(s)):
	        res = res+s[i]*(tot - s[i])
	    res = res//2
	    return int(res%k)

import random
tests = 1
for p in range(tests):
    t = int(1e6)
    if(p<10):
        fi = open('input/input'+'0'+str(p)+'.txt','w')
        fo = open('output/output'+'0'+str(p)+'.txt','w')
    else:
        fi = open('input/input'+str(p)+'.txt','w')
        fo = open('output/output'+str(p)+'.txt','w')
    fi.write(str(t)+'\n')
    q = []
    for i in range(t):
        a,b,c,d = random.randint(-1000000,1000000), random.randint(-1000000,1000000), random.randint(-1000000,1000000), random.randint(-1000000,1000000)
        q.append([a,b,c,d])
        fi.write(str(a)+' '+str(b)+' '+str(c)+' '+str(d)+'\n')
    fo.write(str(main(q))+'\n')
