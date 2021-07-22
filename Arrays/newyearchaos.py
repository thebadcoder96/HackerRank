#https://www.hackerrank.com/challenges/new-year-chaos/problem

q=[2,1,5,3,4]

bribes=0

for i in range(len(q)-1,-1,-1):
    if q[i] - (i+1) > 2: print('Too chaotic')
    for j in range(max(q[i]-2, 0),i):
        if q[j]>q[i]:bribes+=1

print(bribes)