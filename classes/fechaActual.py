import argparse
from calculaFecha import CalculaFecha #En caso de error, revisar la ruta del archivo calculaFecha

if __name__ == "__main__":
	obj1 = CalculaFecha(7,5,2022)
	obj1.calcularFecha(365)
