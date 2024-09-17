vv= input().split(',')
outp=[]
for i in vv:
    if '-' not in i:
        outp.append(int(i))
    else:
        c = i.split('-')
        for j in range(int(c[0]), int(c[1])+1):
            outp.append(j)  
print(*outp)
