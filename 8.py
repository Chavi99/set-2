def cal(l,u):
    for j in range(l+1,u):
        x=str(j)
        p=j
        c=0
        s=0
        for i in x:
            c+=1
        for i in range(c):
            r=j%10
            f=r**c
            s+=f
            j=j//10
        if p==s:
            print(p,end=" ")
m=list(map(int,input().split(" ")))
cal(m[0],m[1])
