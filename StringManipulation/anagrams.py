# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem

from collections import Counter

a='fcrxzwscanmligyxyvym'
b='jxwtrhvujlmrpdoqbisbwhmgpmeoke'
de=0

count_a= Counter(a)
count_b= Counter(b)
count_a.subtract(count_b)


for i in count_a:
    de+=abs(count_a[i])

print(de)

# Bad Solution: 1st solution
# sim=0
# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i]==b[j]:
#             sim+=1
#             break

# print((len(a)-sim)+(len(b)-sim))



