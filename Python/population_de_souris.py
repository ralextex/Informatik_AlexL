Jung=6
Erw=9
Alt=12


for generation in range(5):
    print("generation:",generation,"- Jung: ",Jung,"- Erw: ",Erw,"Alt: ",Alt)
    Jung2=4*Erw+2*Alt
    Alt=int(Erw/3)
    Erw=int(Jung/2)
    Jung=Jung2
