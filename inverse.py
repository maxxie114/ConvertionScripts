IPVL = input("please enter a number\n")
IPVLINB = int(IPVL)
FDG = int(IPVLINB/100)
TDG = int(IPVLINB%10)
SDG = int(IPVLINB/10%10)
RST = FDG*1+SDG*10+TDG*100
if RST < 100:
    if RST < 10:
        RST = RST * 100
    else: 
        RST = RST * 10
print(RST)
