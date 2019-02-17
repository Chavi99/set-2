def cal(n):
    x=int(n)
    p=x
    c=0
    s=0
    for i in n:
        c+=1
    for i in range(c):
        r=x%10
        f=r**c
        s+=f
        x=x//10
    if p==s:
        print("yes")
    else:
        print("no")
m=input()
cal(m)
