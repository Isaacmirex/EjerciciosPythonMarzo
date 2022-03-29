correctos= int(input("Ingrese el numero de aciertos"))
errores= int(input("Ingrese el numero de errores"))
total= correctos+errores
pcorrectos= (100/total)*correctos
pErrores=(100/total)*errores 
print("El puntaje fina "+str(correctos)+"/"+str(total))
print("Su porcentaje en aciertos %.2f"%pcorrectos,"Su porcentaje de Errores %.2f "%pErrores)
