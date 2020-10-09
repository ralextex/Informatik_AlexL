import sys

lines = []
reponse = []
lnombre=[]
L=[]
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
for i in range(1,len(lines)):
    reponse.append(lines[i])
    
reponse.sort()
for x in reponse:
    nombre = reponse.count(x)
    if nombre not in L:
        L=[]
        L.append(nombre)
        L.append(x)
        lnombre.append(L)

lnombre.sort()    

print(lnombre[len(lnombre)-1][1],lnombre[len(lnombre)-2][1] )