def conjugate_guarani_verb(verb, tense):
    """
    Esta función toma un verbo en infinitivo en guaraní y devuelve su conjugación para el tiempo especificado.
    """
    # Diccionario con los prefijos para cada sujeto en presente
    present_prefixes = {
        "Che": "a",
        "Nde": "re",
        "Ha'e": "o",
        "Ñande": "ja",
        "Ore": "ro",
        "Peẽ": "pe",
        "Ha'ekuera": "o",
    }

    # Seleccionar el diccionario de prefijos según el tiempo verbal especificado
    prefixes = present_prefixes

    # Mostrar la conjugación para cada sujeto
    for subject, prefix in prefixes.items():
        conjugated_verb = f"{subject.lower()} {prefix}{verb}'akue"
        print(conjugated_verb.capitalize())

# Ejemplo de uso
if __name__ == "__main__":
    infinitive = input("Ingrese un verbo en infinitivo en guaraní (ej. 'karu'): ")
    tiempo = input("Ingrese el tiempo verbal ('presente' o 'pasado'): ")
    conjugate_guarani_verb(infinitive, tiempo)
