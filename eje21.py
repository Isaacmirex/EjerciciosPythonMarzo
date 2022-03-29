lista1=["a","b","c","d","e"]
lista2=["c","e","f","t","g"]
listaTodo=[]
Lsolo1=[]
Lsolo2=[]
LAmbas=[]
listaTodo=lista1+lista2
for palabra in lista1: 
    if palabra in lista2: 
        LAmbas+=[palabra]
    else:
        Lsolo1+=[palabra]
for palabra in lista2: 
  if palabra not in lista1:
      Lsolo2+=[palabra]
print(lista1)
print(lista2)
print(listaTodo)
print(LAmbas)
print(Lsolo1)
print(Lsolo2)