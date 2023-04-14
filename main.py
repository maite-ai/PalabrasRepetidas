def palabras_repetidas(sentence):
	# Creo un diccionario vacío
	counter = dict()

	# Almacena el string separado por palabras en una lista
	words = sentence.split()

	# Con un for hago un conteo de la aparición de cada palabra
	for word in words:
		counter[word] = counter.get(word, 0)+1

	return counter


def palabra_frecuente(words):
	# Creo e inicializo las variables que la función deberá devolverme
	maxWord = ""
	maxFreq = 0

	# Recorro el diccionario y comparo cuál, de entre todas las frecuencias, es la más alta y la almaceno en las variables
	for word, freq in words.items():
		if freq > maxFreq:
			maxWord = word
			maxFreq = freq
			
	return maxWord, maxFreq
	

sentence = "La clave del crecimiento es seguir creyendo. No te dejes engañar por esa voz negativa en tu cabeza. Sigue creyendo en tu potencial, en tu capacidad para superar obstáculos y en tu institnto para seguir adelante. La misma fuerza que has utilizado para llegar hasta aquí es la que te va a llevar aún más lejos de lo que imaginas"

print("Palabras y su frecuencia de aparición: \n", palabras_repetidas(sentence))
print()
print("Palabra más repetida: ", palabra_frecuente(palabras_repetidas(sentence)))