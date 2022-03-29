lista=[80,34,80,23,70]
pesomaximo=0
peso=0
a=0

for i in range(len(lista)): 
 
    for b in range(len(lista)): 
        if a!=b  :
            peso=lista[a]+lista[b]
            if peso<=150 and peso>0:
                print("Peso de ",lista[a],"+",lista[b],"=",peso)     
       
    a+=1
 
     
    if(pesomaximo<peso): 
        pesomaximo=peso
print("El peso maximo posible es: ", pesomaximo)