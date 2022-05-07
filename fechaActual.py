class FechaActual():

	def __init__(self,dia : int,mes : int,anio : int):
		self.dias31o30 = {1:True,2:False, 3:True, 4:False,5:True,6:False,7:True,8:True,9:False,10:True,11:False,12:True,}
		self.bisiesto = False
		if(anio % 4 == 0):
			self.bisiesto = True
		else:
			self.bisieto = False
		self.dia = dia
		self.mes = mes
		self.anio = anio
		
	def calcularFecha(self, diasAd = int):
		print("La fecha que ingresaste es:", self.dia, "de", self.mes,"de", self.anio,"bandera: ",self.dias31o30[self.mes])
		print("Quieres saber que fecha sera", diasAd ,"dias despues")
		diasContador = self.dia
		#print("Dias totales son: ",diasT)
		#import pdb; pdb.set_trace()
		while (diasAd > 0):
			if(self.mes == 2 and not self.bisiesto): #Bisiesto es de 29 dias
				if(diasContador == 28):
					diasContador = 1
					diasAd = diasAd - 1
					self.mes = self.mes + 1
					continue
			elif(self.mes == 2 and self.bisiesto):
				if(diasContador == 29):
					diasContador = 1
					diasAd = diasAd - 1
					self.mes = self.mes + 1
					continue
			
			if(diasContador == 30 and self.dias31o30[self.mes] == False):
				self.mes = self.mes + 1
				diasContador = 1
				diasAd = diasAd - 1
				continue
				
			if(diasContador == 31):
				self.mes = self.mes + 1
				diasContador = 1
				diasAd = diasAd - 1
				if(self.mes == 13):
					self.mes = 1
					self.anio = self.anio + 1
				continue
					
			
			diasAd = diasAd - 1
			diasContador = diasContador + 1
			#print("diasAd", diasAd)
			#print("diasContador", diasContador)
			
			
		print("La fecha que dio es dia:", diasContador, "mes:",self.mes,"anio:",self.anio)
			

if __name__ == "__main__":
	obj1 = FechaActual(7,5,2022)
	obj1.calcularFecha(365)
