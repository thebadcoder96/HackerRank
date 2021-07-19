#https://www.hackerrank.com/challenges/repeated-string/problem

s="a"
n=10000000000
print(s[:2])
#Count of a in original string
count=s.count('a')

#the string will repeat n//len(s) times plus n%len(s) characters
count *= n//len(s)

#if n%len(s)!=0: count += s[:n%len(s)].count('a')
for i in range(0,n%len(s)):
    if s[i]=='a':count+=1

print(count)

