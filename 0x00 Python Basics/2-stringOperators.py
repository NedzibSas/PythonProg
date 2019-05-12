a,b="Hello","world"
#Operadores de cadenas de caracteres: adición y multiplicación
#Concatenar
msg = a + ' ' + b

#Multiplicar
msg = a*3 #copia 3 veces el contenido de a y los concatena

#Añadir
msg = a
msg +=b #concatena a con b

#Métodos para cadenas de caracteres: buscar, cambiar
#Extensión
tam = len(a) #devuelve el tamaño de a

#Encontrar
find = a.find("l") # '2' devuelve el indice de donde esta lo buscado en la cadena
find = b.find("ld") # '3' si lo buscado no existe, devuelve '-1'

#Minúsculas-Mayúsculas
msg = a.upper() #pasa todo lo de a a mayusculas
msg = b.lower() #

#Reemplazar
msg = a
msg.replace("l", "pizza") # reemplaza 'l' por 'pizza' en el string

#Cortar
msg = a[1:2] # 'e' el primer numero recorta desde el inicio el otro desde el final

#Secuencias de escape
#\t añade tabulacion
#\n salto de linea
