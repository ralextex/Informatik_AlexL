from random import randint
De1=randint(1,6)
De2=randint(1,6)


print("premier lancer:",De1,De2)

Lan1=De1+De2
if Lan1==7 or Lan1==11 :
    print("gagne")
else:
    if Lan1==2 or Lan1==3 or Lan1==12 :
        print("perdu")
    else:
        De3=randint(1,6)
        De4=randint(1,6)
        Lan2=De3+De4
        print("Second lancer:",De3,De4)
        if Lan2==Lan1 :
            print("gagne")
        else:
            print("perdu")
            
