def cal(l,u):
    for i in range(l+1,u):
        if i%2==0:
            print(i,end=" ")
ls=list(map(int,input().split(" ")))
cal(ls[0],ls[1])
