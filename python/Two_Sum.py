# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	dato = int()
	tamano = int()
	target = int()
	print("Ingrese la suma de dos n�meros.")
	target = int(input())
	print("Ingrese la cantidad de n�meros.")
	tamano = int(input())
	print("Ingrese los ",tamano," n�meros.")
	dimnumeros = [int() for ind0 in range(tamano)]
	for i in range(tamano):
		dato = int(input())
		dimnumeros[i] = dato
	for i in range(tamano):
		print("�ndice ",i," contiene: ",dimnumeros[i])
	for i in range(tamano+1):
		for j in range(i+1,tamano):
			if (dimnumeros[i])+(dimnumeros[j])==(target):
				print("El par de n�meros es [",dimnumeros[i],",",dimnumeros[j],"]")
				print("El par de �ndices es [",i,",",j,"]")

