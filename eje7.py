from random import randint
# randint(x,y) numero aleatorio entre x y y 
# random() numero aleatorio entre 0 y 1 
# randrange(x,y,p) numero aleatorio entre x y y pasado por p osea de 2 en dos o cualquier paso que queramos
# uniform(x,y) numero aleatorio entre x y y  de tipo flotante 
zonaUsuario=int(input("ingrese la zona a disparar"))
zonaportero=randint(1,6)
print("La zona del portero fue",zonaportero)
if zonaUsuario==zonaportero:
    print("No ha sido un gol")
else:
    print("Ha sido un gol")