def prime(n):
    for i in range(0,int(n/2)):
        if n%2==0:
            print("no")
            break
    else:
        print("yes")
m=int(input())
prime(m)
