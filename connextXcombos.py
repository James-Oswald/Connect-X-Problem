
import matplotlib as plt

def linear(m,n,s):   
    return (m-s+1)*n+(n-s+1)*m

def diag(m,n,s):   
    return 2*(centeralComp(m,n,s)+sideComp(m,n,s))

def centeralComp(m,n,s):
    return (abs(m-n)+1)*(min(m, n)-s+1)

def sideComp(m,n,s):
    return 2*sum(range(min(m, n)-s+1))

def connectX(m,n,s):
    return linear(m, n, s)+diag(m, n, s)

def printC(m,n,s):
    print(str(m)+","+str(n)+","+str(s)+":"+str(connectX(m,n,s))+","+str(linear(m,n,s))+","+str(diag(m,n,s))+","+str(centeralComp(m,n,s))+","+str(sideComp(m,n,s)))

printC(4, 3, 3)

