#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

n= int(input())
c = list(map(int, input().rstrip().split()))

# Jumping 2 spaces at a time is always going to be min.

# If there are two spaces left and if the two cloud down 
# happens to be an ordinary cloud, jumps two space (2) 
# otherwise jump one (jumping once always)

jumps=0
i=0
while(i< len(c)-1):
    if (i+2<len(c) and c[i+2]== 0) : 
         i+=1
    jumps+=1
    i+=1

print(jumps)
