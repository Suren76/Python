#BRaaibtbritBTsOplr

def rabbits(rab_str):

    rab_char = []

    for char in rab_str:
        if char in "rabbitRABBIT":
            rab_char.append(char)

    #print(rab_char.count("R"))
    #print(rab_char)

    r = rab_char.count("r")+rab_char.count("R")
    a = rab_char.count("a")+rab_char.count("A")
    b = rab_char.count("b")+rab_char.count("B")
    i = rab_char.count("i")+rab_char.count("I")
    t = rab_char.count("t")+rab_char.count("T")

    return(min(r,a,int(b/2),i,t))

    


print(rabbits("BRaaibtbritBTsOplr"))
print(rabbits("RBaitt"))