def cal(l,u):
    for i in range(l+1,u):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i,end=" ")
ls=list(map(int,input().split(" ")))
cal(ls[0],ls[1])
