#Declaramos nuestra lista 3D

temperatura = [
    [  #Arreglo ciudad 1
    [23,15,14,15,18,19,21],
    [15,12,14,25,22,23,26],
    [15,18,19,20,22,26,27],
    [17,19,29,22,22,29,18]
],
    [ #Arreglo ciudad 2
    [25,27,22,23,24,25,26],
    [21,23,24,25,19,18,15 ],
    [24,27,24,23,28,29,25]
    ],
[ #Arreglo ciudad 3
    [24,29,22,27,22,30,25],
    [21,29,24,29,12,18,15 ],
    [33,32,30,25,27,27,27],
    [12,14,17,18,22,25,24]

    ]
]

semana = 1
dia = 1

#Creamos las variables y las inicializamos
suma = 0
contador = 0



for i in range(len(temperatura)): #Recorremos nuestra lista
    if i == semana: #Comprobamos si al recorrer i una iteración es igual a semana
        for j in range(len(temperatura[i])): # Recorremos los dias dentro de nuestra lista ciudad actual
            if j == dia : #Comprobamos si al recorrer j una iteración es igual a dia
                 for k in range(len(temperatura[i][j])):  #La iteración temperatura recorre cada temperatura registrada en el día actual.
                    suma+= temperatura[i][j][k]
                    contador += 1  # Aumentamos en uno nuestro contador



# Calculamo  el promedio si se cumple nuestra condicional
if contador > 0:
    promedio = suma / contador #Calculamos promedio
    print(f"El promedio de la ciudad {semana+1} de la semana {dia+1} es: {promedio}") #Imprimimos el resultado
else:
    print("No se puede calcular .")