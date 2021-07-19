#https://www.hackerrank.com/challenges/sock-merchant/problem

n= int(input())
ar = list(map(int, input().rstrip().split()))
pairs = 0
ar.sort()
for i in range(n):
    for j in range(i+1, n):
        if (ar[i]==ar[j]):
            pairs+=1
            ar[j]=0
            break
        
print(pairs)