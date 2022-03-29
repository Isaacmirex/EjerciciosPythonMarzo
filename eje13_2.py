frase= input("Ingrese una frace: ")
letra= input("la letra abuscar: ")
cont=0
for carac in frase: 
    if carac==letra: 
        cont+=1
if cont>0:
    print("La letra"+letra+"se encontro: "+str(cont)+" veces")
else:
    print("no se encontro la letra "+ str(letra))
    