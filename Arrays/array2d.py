#https://www.hackerrank.com/challenges/2d-array/problem

arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

count = -64
row = 0
col = 0
while row < 4 :
    temp = arr[row][col] + arr[row][col+1]+arr[row][col+2]
    temp+= arr[row+1][col+1]
    temp+= arr[row+2][col]+arr[row+2][col+1]+ arr[row+2][col+2]
        
    count=max(count,temp)
    col +=1
    if col == 4:
        col = 0
        row +=1
print(count)