#Calculadora de edad

import datetime as dt

fecha_de_nacimiento = dt.datetime.strptime(input("Ingresa tu fecha de nacimiento en este formato: DD/MM/AAAA "), "%d/%m/%Y")

fecha_actual = dt.datetime.now()

calcular_edad = fecha_actual - fecha_de_nacimiento

print(calcular_edad)
