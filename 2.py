n= int(input())
b=[int(x) for x in input().split()]
bb=b
ans=[1]
if bb[0] == -1:
    bb[0] +=2
for j in range(1, len(b)):
    if b[j] == -1:
        bb[j] = bb[j-1]+1
    ans.append(bb[j] - bb[j-1])    
for i in range(1, n):
    if bb[i-1] > bb[i]:
        print('NO')
        exit()
print('YES')

print(*ans)
        