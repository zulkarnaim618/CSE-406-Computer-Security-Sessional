import math
import random
import sympy
import time

def generateRandomCurve(p):
    while True:
        a = random.randrange(2,100)
        b = random.randrange(2,100)
        if (4*a*a*a+27*b*b)%p!=0:
            break
    return (a,b)



def makeData(a,length):
    s = format(a,'b').rjust(length,'0')
    l = []
    for i in range(0,len(s),8):
        a = int(s[i:i+8],2)
        l.append(a)
    return l

def pointAddDouble(g,a,n,p):
    n = format(n,'b')
    v = [g[0],g[1]]
    for i in n[1:]:
        s = ((3*v[0]*v[0]+a)*pow(2*v[1],-1,p))%p
        x = (s*s-v[0]-v[0])%p
        y = (s*(v[0]-x)-v[1])%p
        v = [x,y]
        if i=='1':
            s = ((v[1]-g[1])*pow(v[0]-g[0],-1,p))%p
            x = (s * s - v[0] - g[0]) % p
            y = (s * (g[0] - x) - g[1]) % p
            v = [x, y]
    return (v[0],v[1])

def mem_s_i(i,x,p):
    return pow(x,(p-1)>>i,p) == 1

def tonelli_sqrt(c,p):
    if c%p ==0:
        return [0]
    if not mem_s_i(1,c,p):
        return []
    q = p-1
    ell = 0
    while q%2==0:
        ell = ell +1
        q = q//2
    while True:
        n = random.randrange(1,p)
        if not mem_s_i(1,n,p):
            break
    ninv = pow(n,p-2,p)
    e = 0
    for i in range(2,ell+1):
        if not mem_s_i(i,pow(ninv,e,p)*c,p):
            e = e +2**(i-1)
    a = pow(pow(ninv,e,p)*c,(q+1)//2,p)
    b = (pow(n,e//2,p)*a)%p
    return [b,p-b]

def generateRandomPoint(a,b,p):
    x = 0
    y = []
    while len(y) == 0:
        x = random.randrange(0, p)
        y = tonelli_sqrt(x * x * x + a * x + b, p)
    y = y[0]
    return (x,y)



def main():
    print("\tComputation Time For")
    print("k\t\t\tA\t\t\tB\t\t\tshared key R")
    for length in [128,192,256]:
        trialNum = 5
        aTime = 0
        bTime = 0
        rTime = 0
        for j in range(0,5):
            p = sympy.randprime(pow(2, length - 1), pow(2, length))
            #p = 17
            (a,b) = generateRandomCurve(p)
            #(a,b) = (2,2)
            #g = (5,1)
            g = generateRandomPoint(a,b,p)
            ka = random.randrange(2,int(p+1-2*math.sqrt(p)))
            kb = random.randrange(2,int(p+1-2*math.sqrt(p)))
            startTime = time.time()
            kag = pointAddDouble(g,a,ka,p)
            aTime += (time.time() - startTime)*1000
            startTime = time.time()
            kbg = pointAddDouble(g,a,kb,p)
            bTime += (time.time() - startTime)*1000
            startTime = time.time()
            kabg = pointAddDouble(kag, a, kb, p)
            rTime += (time.time() - startTime)*1000
        print(str(length)+"\t"+str(aTime/trialNum)+" ms\t"+str(bTime/trialNum)+" ms\t"+str(rTime/trialNum)+" ms")

if __name__ == "__main__":
    main()