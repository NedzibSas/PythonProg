import sys

#funcion print nativa de alto nivel
#uso de \ para caracteres "especiales" o "reservados" "\""
print("Hello world")
print("\"Special\"")

#imprimir una variable bajo un formato determinado
#uso de {} para indicar la ubicacion de la variable en el mensaje
#d=int, f=float, c=char
number = 98
print("{:d} Integer format print".format(number))

#usar {:.2f} para restringir el numero de decimales que se imprime
print("{:.2f} Float format print".format(number))

#char 98 = 'b'
print("{:c} Char format print".format(number))

#print de 2 strings utilizando la funcion format para
#imprimir 3 veces la cadena, y luego restringir el tamaño de la
#cadena al imprimirla
str = "This is a String"
print("{}\n{}".format(str * 3, str[0:9]))

#print a nivel de interprete(?
sys.stderr.write("Interpreter print\n")
sys.exit(1)