from random import randint 
ganadas=0
ganadasMaquina=0
scoreMA=0
scoreU=0
def ppt(op): 

    if op==1: 
        r="Piedra"
    elif op==2: 
        r="Papel"
    elif op==3: 
        r="Tijera"
    return r
  
while ganadas<3 and ganadasMaquina<3: 
    opUsuario = int (input("Ingresa una opcion:\n1.-piedra\n2.-papel\n3.-tijera\ningrese la opcion: "))
    opMaquina = randint(1,3)
    if opUsuario>3 or opUsuario<1: 
        continue
    print("El usuario elige: ",ppt(opUsuario))
    print("La maquina elige: ",ppt(opMaquina))
    if (opUsuario==1 and opMaquina==3) or (opUsuario==2 and opMaquina==1) or (opUsuario==3 and opMaquina==2) : 
        print("GANA EL USUARIO")
        ganadas+=1
        scoreU+=1
    elif opUsuario==opMaquina:
        print("EMPATE")
    else: 
        scoreMA+=1
        ganadasMaquina+=1
        print("LA MAQUINA GANA ")
    print("EL score Usuario: ",scoreU,"El score Maquina: ",scoreMA)
    print()
    
