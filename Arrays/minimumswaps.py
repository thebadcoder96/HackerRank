#https://www.hackerrank.com/challenges/minimum-swaps-2/problem

arr=[2,3,4,1,5]
sr=sorted(arr)
c=0

for i in range(len(arr)):
    if (arr[i]!=sr[i]):
        ix=arr.index(sr[i])
        arr[i],arr[ix]=arr[ix],arr[i]
        c+=1

print(arr,c)