import sys
sys.path.insert(0,"./classes/") #En caso de error, revisar la ruta en donde estaran las clases
from calculaFecha import CalculaFecha #En caso de error, revisar la ruta del archivo calculaFecha

if __name__ == "__main__":
	obj1 = CalculaFecha(7,5,2022)
	obj1.calcularFecha(365)
