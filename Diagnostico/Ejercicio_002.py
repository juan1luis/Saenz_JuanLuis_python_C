nombre = input('¿Cuál es tu nombre(s)?')
apellido = input('¿Cuál es tu primer apellido?')
se_apellido = input('¿Cuál es tu segundo apellido?')
año_na = input('¿En qué año naciste?')
mes_dia_na = input('¿En qué mes y día naciste? (en el siguiente formato “mm-dd”)')
año_actual = 2022
_vocales = ['a','e','i','o','u']

nombre_completo = nombre + ' ' + apellido + ' ' + se_apellido
nombre_minusculas = nombre_completo.lower()
nombre_mayusculas = nombre_completo.upper()
edad = año_actual - int(año_na)
vocales = 0
letras = 0
for i in nombre_minusculas:
    if i in _vocales:
        vocales += 1
    else:
        letras +=1

print('Este es tu nombre completo en mayúsculas: ' + nombre_mayusculas)
print('Este es tu nombre completo en minúsculas:' + nombre_minusculas)
print('Esta es tu fecha de nacimiento: ' + mes_dia_na[3:] + '-' + mes_dia_na[:2] + "-" + str(año_actual))
print('Esta es tu edad: ' + str(edad) )
print('Tu nombre completo tiene '+ str(vocales) +' vocales')
print('Tu nombre completo tiene ' + str(letras) + ' letras')
print('¿Tu edad es un carácter de tipo número?' + str(str(edad).isdigit()))
print('¿Tu nombre completo es un carácter de tipo alfanumérico? ' + str(not str(nombre_completo).isdigit())) 
print('Tu edad en 10 años será: ' + str( edad + 10))
print('La media de tu edad actual y tu edad en 20 años es: ' + str(edad/2) + ' ' + str((edad+20)/2))