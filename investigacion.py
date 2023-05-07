import csv

class Pasta:
	__tipo_pasta = ''
	__marca = ''
	__peso = ''
	__valor = ''

	def __init__(self,tipo,marca,peso,valor):
		self.__tipo_pasta = tipo
		self.__marca = marca
		self.__peso = peso
		self.__valor = valor

	def GetTipo(self):
		return self.__tipo_pasta
	
	def GetMarca(self):
		return self.__marca
	
	def GetPeso(self):
		return self.__peso
	
	def GetValor(self):
		return self.__valor
		
	def __eq__(self,cad):
		if cad == self.__tipo_pasta:
			return self.__tipo_pasta
		elif cad == self.__marca:
			return self.__marca
		elif cad == self.__peso:
			return self.__peso
		elif cad == self.__valor:
			return self.__valor

if __name__ == "__main__":
	lista_pasta = [] #Declaramos la lista
	archivo = open('pastas.csv') #Abrimos el archivo CSV
	reader = csv.reader (archivo,delimiter = ",") #Leemos el archivo
	for fila in reader:
		unaPasta =  Pasta(fila[0],fila[1],fila[2],fila[3]) #Cargamos la lista
		lista_pasta.append(unaPasta) #Se agrega el objeto creado
	archivo.close()
	
	lista_pasta2 = [] #Declaramos la lista
	archivo = open('pastas2.csv') #Abrimos el archivo CSV
	reader = csv.reader (archivo,delimiter = ",") #Leemos el archivo
	for fila in reader:
		unaPasta2 =  Pasta(fila[0],fila[1],fila[2],fila[3]) #Cargamos la lista
		lista_pasta2.append(unaPasta2) #Se agrega el objeto creado
	archivo.close()
	lista_pasta.extend(lista_pasta2) #Se unen las 2 listas, lista 1 y 2
	
	for i in range(len(lista_pasta)):
		print(f"[Tipo de pasta]: {lista_pasta[i].GetTipo()} [Marca de pasta]: {lista_pasta[i].GetMarca()} [Peso de la pasta]: {lista_pasta[i].GetPeso()} [Valor de la pasta]: {lista_pasta[i].GetValor()}")
	print(f"\nCantidad de pastas marca luchetti: {lista_pasta.count('Luchetti')}")
		
