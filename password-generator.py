import random
import string

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

def main():
    print("**Generador de Contraseñas Seguras**")
    longitud = int(input("introduce la longitud de la contraseña: "))
    contraseña = generar_contraseña(longitud)
    print(f"Tu nueva contraseña es: {contraseña}")

if __name__ == "__main__":
    main()

// Revisar
// contraseña = "ranyan"
// usuario = input()
// while usuario != contraseña:
    // usuario = input()
// print("Permiso concedido")
