import sys
sys.path.insert(0,"./classes/") #En caso de error, revisar la ruta en donde estaran las clases
from CalculaFecha import CalculaFecha #En caso de error, revisar la ruta del archivo calculaFecha
import Parser

if __name__ == "__main__":
	dia = Parser.args.dia
	mes = Parser.args.mes
	anio = Parser.args.anio
	diasSumados = Parser.args.calcD
	obj1 = CalculaFecha(dia,mes,anio)
	obj1.calcularFecha(diasSumados)
