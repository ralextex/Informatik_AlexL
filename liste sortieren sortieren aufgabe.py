from random import randint
L=[]
summe=[]
        
for füllung in range (5):
    K=[]
    for füllung2 in range(randint(5,15)):
        r=randint(1,50)
        K.append(r)
    L.append(K)  


for list in L:
    nichtsortiert=True
    while nichtsortiert:
        for k in range(1,len(list)):
            nichtsortiert=False
            if list[k-1]>list[k]:
                swap=list[k-1]
                list[k-1]=list[k]
                list[k]=swap
                nichtsortiert=True
                break
    s=0
    for m in list:
        s+=m
        
    summe.append(s)

ptrier=True
while ptrier:
    for d in range(1,len(L)):
        ptrier = False
        if summe[d-1]>summe[d]:
            swap=L[d-1]
            L[d-1]=L[d]
            L[d]=swap
            swap2=summe[d-1]
            summe[d-1]=summe[d]
            summe[d]=swap2
            ptrier = True
            break
    

for zeile in L:
    print(zeile)    
print(summe)
