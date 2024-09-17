l, r = input().split()
l, r = int(l), int(r)
count=0
for j in range(l, r+1):
    a=0
    for i in range(2, int(j//2)+1):
        if j%i==0:
            a+=1
    if a!=0:
        flag = True
        for i in range(2, int(a+2//2)+1):
            if (a+2)%i==0:
                flag = False
                break
        if flag:
            count+=1
            
print(count)
