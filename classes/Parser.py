import argparse

descripcion="Este programa lee una fecha y número entero. Y regresa otra fecha calculada\
			en base a la fecha introducida más el número entero"

parser = argparse.ArgumentParser(description=descripcion)
parser.add_argument('-d', metavar='<Dia>', type=int,
                    help='El dia en donde partirá el calculo de la fecha', dest="dia",
                    required=True)
parser.add_argument('-m', metavar='<Mes>', type=int,
                    help='El mes en donde partirá el calculo de la fecha',dest="mes",
                    required=True)
parser.add_argument('-a', metavar='<Año>', type=int,
                    help='El año en donde partirá el calculo de la fecha',dest="anio",
                    required=True)
parser.add_argument('-c', metavar='<Dias a calcular>', type=int,
                    help='Los dias a calcular a partir de la fecha establecida',
                    dest="calcD",required=True)  
          
args = parser.parse_args()

