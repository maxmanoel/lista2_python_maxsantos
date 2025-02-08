#Escrevaum programa que solicite uma determinada de numeros de dias, em eguida exiba o quanto esses dias equivalem em horas minutos e segundos 
dias=int(input("Digite quantos dias foram: "))
hora = dias *24
minutos = hora*60
segundos = minutos*60
print (dias, "dia", hora, "horas", minutos, "minutos", segundos, "segundos")
