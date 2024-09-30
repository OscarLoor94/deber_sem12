#Creamos nuestro diccionario en donde vamos a colocar cable - valor
informacion_personal = {"Nombre":"Lucas", "Edad":28,"Ciudad": "Santo Domingo","Email":"Lucasruiz@gmail.com","Profesión": "Cantante"}

#Imprimimos el diccionario actual
print("\nDiccionario actual \n",informacion_personal)


#Modificamos el valor Ciudad
informacion_personal.update({"Ciudad": "Quito"})



#Agregamos una nueva clave-valor al diccionario que represente la profesión de la persona.

informacion_personal.update({'Profesión':'Ingeniero en Software'})
print(f"Se cambio la profesion")

#Verificamos si la clave telefono existe
telf = input("Ingrese el nombre de la clave : ")  #Se ingresa si existe telefono
if telf in informacion_personal :  #Con un if verificamos si existe

    print("Si existe la clave de teléfono")  #Mandamos un mensaje
else:
    print(f"No existe la clave {telf} ")  # Imrprimimos un mensaje que no existe la clave
    num_tel = int(input(f"Ingrese un numero a {telf}: "))  # El usuario ingresa el numero
    informacion_personal[telf] = num_tel  # Creamos la clave telefono y el valor del numero de telofono que ingreso
    print("\nClave y valor agregado correctamente ")


#Eliminamos la clave edad
informacion_personal.pop("Edad")
print("\nEdad Eliminada")

#Imprimimos el diccionario despues de haber hecho las modificaciones
print(f"\n\nDICCIONARIO ACTUALIZADO \n {informacion_personal}")