def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multiplicacion(a,b):
    return a * b
def division(a,b):
    if b != 0:
        return a / b
    else:
        return "No se puede dividir por cero"
    
print("Calculadora Básica")
a = float(input("Ingresa el primer numero: "))
b = float(input("Ingresa el segundo numero: "))

print("Suma: ", suma(a,b))
print("Resta: ", resta(a,b))
print("Multiplicación: ", multiplicacion(a,b))
print("División: ", division(a,b))
