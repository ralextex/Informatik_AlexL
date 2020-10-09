from random import randint

N=100000

counta=0
countb=0

for test in range(N):
    attack=[]
    defens=[]
    for i in range(3):
        a=randint(1,6)
        attack.append(a)
    for k in range(2):
        d=randint(1,6)
        defens.append(d)

    ptrier=True
    while ptrier:
        for f in range(1,len(attack)):
            ptrier = False
            if attack[f-1]>attack[f]:
                swap=attack[f-1]
                attack[f-1]=attack[f]
                attack[f]=swap
                ptrier = True
                break

    ptrier=True
    while ptrier:
        for p in range(1,len(defens)):
            ptrier = False
            if defens[p-1]>defens[p]:
                swap=defens[p-1]
                defens[p-1]=defens[p]
                defens[p]=swap
                ptrier = True
                break

    if(attack[2]>defens[1]):
        counta+=1
    else:
        countb+=1


    if(attack[1]>defens[0]):
        counta+=1
    else:
        countb+=1
    

print("attack:",counta/N,"defenseur:",countb/N)
