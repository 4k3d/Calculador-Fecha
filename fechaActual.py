import argparse
from calculaFecha import CalculaFecha #Importo mi clase desde otro archivo

if __name__ == "__main__":
	obj1 = CalculaFecha(7,5,2022)
	obj1.calcularFecha(365)
