n = int(input())
s=[]
for i in range(n):
    s.append(list(map(int, input().split())))
proc = dict()
for i in range(n):
    if len(s[i]) == 1:
        proc[i+1] = int(s[i][0]) 
    else:
        ma=0
        for j in (s[i][1:]):
            ma=max(int(proc[j+1]),ma)
        proc[i+1]= int(s[i][0])+ma

