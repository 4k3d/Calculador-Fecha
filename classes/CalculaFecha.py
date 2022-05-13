class CalculaFecha():

	def __init__(self,dia : int,mes : int,anio : int):
		
		self.dias31o30 = {1:True,2:False, 3:True, 
		4:False,5:True,6:False,7:True,8:True,
		9:False,10:True,11:False,
		12:True,} #Diccionario en donde guardo que meses tienen 31 dias (True) o menos de 31 (false)		
		self.bisiesto = False #Bandera para saber si estoy en un año bisiesto		
		if(anio % 4 == 0): #Condicional para setear la bandera en un estado inicial
			self.bisiesto = True
		else:
			self.bisieto = False
		self.dia = dia
		self.mes = mes
		self.anio = anio
		
	def calcularFecha(self, diasAd = int):
		print("La fecha que ingresaste es:", self.dia, "de", self.mes,"de", self.anio)
		print("Quieres saber que fecha sera", diasAd ,"dias despues")
		while (diasAd > 0):
			if(self.mes == 2 and not self.bisiesto): #Bisiesto es de 29 dias
				if(self.dia == 28):
					self.dia = 1
					diasAd = diasAd - 1
					self.mes = self.mes + 1
					continue
			elif(self.mes == 2 and self.bisiesto):
				if(self.dia == 29):
					self.dia = 1
					diasAd = diasAd - 1
					self.mes = self.mes + 1
					continue
			
			if(self.dia == 30 and self.dias31o30[self.mes] == False):
				self.mes = self.mes + 1
				self.dia = 1
				diasAd = diasAd - 1
				continue
				
			if(self.dia == 31):
				self.mes = self.mes + 1
				self.dia = 1
				diasAd = diasAd - 1
				if(self.mes == 13):
					self.mes = 1
					self.anio = self.anio + 1
					if(self.anio % 4 == 0): 
						self.bisiesto = True
					else:
						self.bisieto = False
				continue
					
			
			diasAd = diasAd - 1
			self.dia = self.dia + 1
			#Fin del scope del while#
						
		print("La fecha que dio es dia:", self.dia, "mes:",self.mes,"anio:",self.anio)

