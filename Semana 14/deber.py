
lista =[] #Creamos la lista
suma = 0  #Declaramos suma en cero
while True:   #El bucle while se reptira miestras cont sea menor a los porductos que decidimos ingresar
        valor = float(input("Ingrese el valor: "))  #Ingresamos los valores
        lista.append(valor) #Agregamos a la lista los valores
        suma = suma + valor  #Sumamos los valores


        pro = input("¿ Desea ingresar mas valores ?")  #Preguntamos si desea volver a ingresar mas valores
        if pro == "no":  # Si elije no se detiene
            break


print("\nVALORES ")
print(lista)  #Imprimimos los valores

descuento_f = int(input("Ingrese el descuento: "))  #Creamos la variable descuento




def p_final (monto,descuento): #Creamos la función con 2 parametros monto y descuento

    desc = monto -  (monto * descuento / 100)  # Calculamos el descuento restando el porcentaje menos el monto
    return desc  #Retornamos el descuento

print(f"El monto total es de {suma},el descuento es del {descuento_f}% y el valor total a pagar es de $ {p_final(suma,descuento_f)} dolares"  )#Llamamos a nuestra función e imprimimos


