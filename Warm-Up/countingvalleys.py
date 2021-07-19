#https://www.hackerrank.com/challenges/counting-valleys/problem

steps=int(input())
path=input()

res=0
ans=0
for i in range(steps):
    if (path[i]=='U'): 
        res+=1
    else:
        res-=1
    if (path[i]=='U' and res==0):
        ans+=1
print(ans)