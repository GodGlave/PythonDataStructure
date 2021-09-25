def Hanoi(n,a,b,c):
    if n > 0:
        Hanoi(n-1,a,c,b)
        print("moving from %s to %s"%(a,c))
        Hanoi(n-1,b,a,c)

Hanoi(3,'A','B','C')