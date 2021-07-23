# https://www.hackerrank.com/challenges/alternating-characters/problem

s="AABAAB"
c=0

for i in range(len(s)-1):
    if s[i]==s[i+1]:
        p=s.replace(s[i+1],'')
        c+=1

print(c)
