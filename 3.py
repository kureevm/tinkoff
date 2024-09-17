from itertools import product
a= input()
b= input()
k= int(input())
a1 = list(map(''.join, product(b, repeat = k)))
ans=[]
for i in a1:
    if i in a:
        ans.append(i)
print(ans[-1])