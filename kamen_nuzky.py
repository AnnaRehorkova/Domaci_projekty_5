from random import randrange

tah_hrace = input("Zadej kámen, nůžky nebo papír (pro ukončení hry napiš 'konec'): ")
while tah_hrace != "konec":

    cislo = randrange(3)
    if  cislo == 0:
        tah_pocitace = "kámen"
    elif cislo == 1:
        tah_pocitace = "nůžky"
    else:
        tah_pocitace = "papír"



    if tah_hrace == tah_pocitace:
        print("Plicha.")
    elif (tah_hrace == "kámen" and tah_pocitace !="papír") or (tah_hrace == "papír" and tah_pocitace !="nůžky") or (tah_hrace == "nůžky" and tah_pocitace!="kámen"):
        print("Vyhrála jsi!")
    elif (tah_hrace == "kámen" and tah_pocitace =="papír") or (tah_hrace == "papír" and tah_pocitace =="nůžky") or (tah_hrace == "nůžky" and tah_pocitace =="kámen"):
        print("Počítač tě dostal!")
    elif tah_hrace == "konec":
        tah_hrace == False
    else:
        print("Nerozumím, zkus to znovu.")

    print("Použila jsi:", tah_hrace)
    print("Počítač použil:", tah_pocitace)
    tah_hrace = input("Zadej kámen, nůžky nebo papír (pro ukončení hry napiš 'konec'): ")




"""
if  tah_hrace == "kámen":
    if tah_pocitace == "kámen":
        print("Plichta.")
    elif tah_pocitace == "nůžky":
        print("Vyhrál jsi!")
    elif tah_pocitace == "papír":
        print("Počítač tě dostal!")

elif tah_hrace == "nůžky":
    if tah_pocitace == "kámen":
        print("Počítač tě dostal")
    elif tah_pocitace == "nůžky":
        print("Plichta.")
    elif tah_pocitace == "papír":
        print("Vyhrál jsi!")

elif tah_hrace == "papír":
    if tah_pocitace == "kámen":
        print("Vyhrál jsi!")
    elif tah_pocitace == "nůžky":
        print("Počítač tě dostal")
    elif tah_pocitace == "papír":
        print("Plichta.")
"""
