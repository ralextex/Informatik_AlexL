from random import randint

L=[]
for i in range(10):
    r=randint(1,1000)
    L.append(r)

ptrier=True
while ptrier:
    for d in range(1,len(L)):
        ptrier = False
        if L[d-1]>L[d]:
            swap=L[d-1]
            L[d-1]=L[d]
            L[d]=swap
            ptrier = True
print(L)
            
    
