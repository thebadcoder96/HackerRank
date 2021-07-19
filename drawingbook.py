#https://www.hackerrank.com/challenges/drawing-book/problem

n = int(input())
p = int(input())

#Total pages and pages to turn from front
totalp = n//2
page = p//2

#if page number is 1, then 0 turns
if (p==1): result=0
else:
    back=totalp-page
    result = min(page, back)

print(result)