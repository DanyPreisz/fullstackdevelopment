Algoritmo termina_en_4
	Definir num Como entero;
	Escribir 'Ingrese un n�mero';
	Leer num;
	Si (num mod 10 = 4) Entonces
		Escribir "El n�mero termina en 4";
	SiNo
		si(num mod 10 = -4) entonces
			Escribir "El n�mero termina en 4";
		SiNo
			Escribir "El n�mero no termina en 4";
		finsi
	FinSi
FinAlgoritmo
