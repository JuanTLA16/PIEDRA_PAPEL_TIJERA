

import random


print("----------------------------------------")
print("--------PIEDRA PAPEL O TIJERA-----------")
print("----------------------------------------")




print(" 1 -------> Piedra ")
print(" 2 -------> Papel ")
print(" 3 -------> Tijera ")

PIEDRA = 1
PAPEL = 2
TIJERA = 3

opcion = int(input("Digite cual quiere que sea su personaje de batalla =)  :  "))
MAQUINA = random.randint(1, 3)
if (MAQUINA==1):
    rta2 = " El personaje de la maquina es PIEDRA"
elif (MAQUINA==2):
    rta2 = " El personaje de la maquina es PAPEL"
elif (MAQUINA==3):
    rta2 = "El personaje de la maquina es TIJERA"

if (opcion==1):
    rta = "Su personaje es PIEDRA"
elif (opcion==2):
    rta= "Su personaje es PAPEL"
elif (opcion==3):
    rta= "Su personaje es TIJERA"

if ( opcion==PIEDRA and MAQUINA==PAPEL):
    print("El ganador es TERMINATOR")
elif(opcion==PIEDRA and MAQUINA==TIJERA):
    print("El ganador es JUANCHO")
elif(opcion==PIEDRA and MAQUINA==PIEDRA):
    print("JUANCHO y TERMINATOR quedaron empate")
elif(opcion==PAPEL and MAQUINA==PIEDRA):
    print("El ganador es JUANCHO")
elif(opcion==PAPEL and MAQUINA==TIJERA):
    print("El ganador es TERMINATOR")
elif(opcion==PAPEL and MAQUINA==PAPEL):
    print("JUANCHO y TERMINATOR quedaron empate")
elif(opcion==TIJERA and MAQUINA==PAPEL):
    print("El ganador es JUANCHO")
elif(opcion==TIJERA and MAQUINA==PIEDRA):
    print("EL ganador es TERMINATOR")
elif(opcion==TIJERA and MAQUINA==TIJERA):
    print("JUANCHO y TERMINATOR quedaron empates")


   

# MAQUINA





print("El personaje de combate de la MAQUINA es: " + str(rta2))
print("Su personaje de combate es : " + str(rta))



