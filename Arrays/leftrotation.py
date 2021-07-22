#https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
d = int(first_multiple_input[1])
a = list(map(int, input().rstrip().split()))


temp=[]
temp2=[]

for i in range(d):
    temp.append(a[i])

while d<n:
    temp2.append(a[d])
    d+=1

print(temp2+temp)