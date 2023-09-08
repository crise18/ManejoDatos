# -*- coding:utf-8 -*-
import random
import time


##########################################################
# Manejo de Datos
# Práctica 1
# Equipo: 
##########################################################

##########################################################
# Ejercicio 1
#
##########################################################
def desviacion_estandar(mi_archivo):
	""" Lee los datos de mi_archivo y calcula la desviación estandar
	de los montos totales
	:param mi_archivo: str, Ruta del archivo 'ventas.txt'
	:returns: float, valor calculado de la desviación estandar
	"""
	ventas = open(mi_archivo, "r")  # Abre el archivo deseado

	conjunto_datos = []
	# Lee cada línea del archivo
	for linea in ventas:
		linea = linea.strip()  # Eliminamos posibles espacios
		# Esto nos permitira generar listas por linea a través del for
		datos = linea.split(
			",")  # Usando la función split vista en clase generamos un lista, separando cada dato por una coma.
		conjunto_datos.append(datos)  # Agrega la lista de datos a la lista total de datos

	# Calculemos la desviación estandar
	# Promedio de los montos totales
	suma = 0
	for i in range(len(conjunto_datos)):
		suma += float(conjunto_datos[i][3])  # Recorremos las lineas y sumamos el cuarto elemento, en el txt
	promedio = suma / len(conjunto_datos)

	# Absoluto de diferencias
	absoluto = []
	for i in range(len(conjunto_datos)):
		absoluto.append(abs(float(conjunto_datos[i][3]) - promedio))

	# Calculemos la suma de los cuadrados de los absolutos
	suma_abs = 0.0

	for i in range(len(conjunto_datos)):
		suma_abs += absoluto[i] ** 2

	# Calculemos la desviacion estándar
	dev_stan = pow(suma_abs / len(conjunto_datos), 1 / 2)

	return dev_stan

	# print(conjunto_datos)

	# Así podremos accesar a nuestra tipo de dato buscado a través de un sistema tipo matriz, renglon-columna.

##########################################################
# Ejercicio 2
##########################################################
#
# inciso a)
##########################################################
def monkey(cadena_objetivo):
	""" Genera cadenas pseudoaleatorias de tamaño igual a la cadenda_objetivo
	:param cadena_objetivo: str, Cadena a la que deseamos llegar tecleando de forma aleatoria
	:returns: str, Cadena pseudoaleatoria generada 
	"""
	letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's',
			  't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
	orig = "methinks it is like a weasel"
	cadena_generada = ""
	i = 0
	while i <  len(orig):
		cadena_generada += random.choice(letras)
		i += 1
	return cadena_generada

##########################################################
# inciso b)
#
##########################################################
def count_coincidencias(cadena_generada, cadena_objetivo):
	""" Cuenta las coincidencias entre caracteres de las cadenas dadas.
	:param cadena_generada: str, Cadena generada de forma aleatoria
	:param cadena_objetivo: str, Cadena a la que deseamos llegar tecleando de forma aleatoria
	:returns: int, coincidencias encontradas
	"""
	coincidencias = 0
	for i in range(len(cadena_generada)):
		if cadena_generada[i] == cadena_objetivo[i]:
			coincidencias += 1

	return coincidencias

##########
#Calculo del máximo de coincidencias
##########
# def maximo(original:int, nueva:int, cadena_generada:str):
# 	coincidencia_max = 0
# 	cadena_maxima = ""
# 	if nueva >= original:
# 		concidencia_max = nueva
# 		cadena_maxima = cadena_generada
# 	else:
# 		coincidencia_max = original
# 	return coincidencia_max, cadena_generada

##########################################################
# inciso c)
#
##########################################################
def infinit_monkey():
	""" Simula el mono tecleando de forma aleatoria hasta teclear la cadena objetivo = "methinks it is like a weasel"
	:returns: None, 
	"""
	cadena_generada = ""
	cadena_origen = "methinks it is like a weasel"
	cadena_maxima = ""
	maximo = 0
	a = ""
	contador = 0
	while cadena_generada != cadena_origen:
		cadena_generada = str(monkey(cadena_origen)) #Creamos la cadena nueva
		coincidencias = int(count_coincidencias(cadena_generada, cadena_origen)) #Contamos las coincidencias
		#coincidencias_max = maximo(maximo_base, coincidencias, cadena_generada)
		#Veamos cual es la concidencia maxima y su cadena
		if coincidencias > maximo:
			maximo = coincidencias
			cadena_maxima = cadena_generada
		else:
			cadena_maxima = cadena_maxima

		#Si quremos LIMITAR las iteraciones
		#if contador == 100000:
		#	cadena_generada = cadena_origen
		contador += 1

		#print(f" Máximo:", maximo, "Cadena Maxima:", cadena_maxima)
		print("Maximo:", maximo, "Cadena Maxima:", cadena_maxima)
		print("Cadena generada:", cadena_generada)
		print(f"Cadena objetivo:", cadena_origen)
		print(f"Coincidencias actuales:", coincidencias, " de 28")
		print(f"Iteracion:", contador)
		print("------------------------------------------------------")

		#time.sleep(.1)
def main():
	seleccion = 0
	while seleccion != 3:
		print("-----------------------------------------------------")
		print("BIENVENID@ a la primer práctica de Manejo de Datos!")
		print("Lista de opciones")
		print("  1. Programa. Mono infinito\n  2. Programa. Desviación estandar\n  3. Salir")
		print("-----------------------------------------------------")
		print("ADVERTENCIA: El programa del mono infinito, nunca termina, por lo tanto, sera necesario abortar la \n"
			  "operacion si desea detener el programa!")
		print("   Nota. En la parte del código se propuso un contador, para que el programa se aborte después de \n "
			  "  cierto número de repeticiones, además se añadio un contador para saber en que iteración vamos.")
		seleccion = input("-> Seleccione la opción deseada: ")
		if(seleccion == "1"):
			print(infinit_monkey())
			seleccion = "0"
		if(seleccion == "2"):
			print("********************************************")
			print("Nombre del archivo = ventas.txt")
			name_archivo = input("Ingrese el nombre de su archivo junto con su extensión: ")
			DEV = desviacion_estandar(name_archivo)
			print(f"DE =", desviacion_estandar(name_archivo))
			print("********************************************")
			seleccion = "0"
		if(seleccion == "3"):
			print("Nos vemos!")
			break

if __name__ == "__main__":
    main()



