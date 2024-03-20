def calculadora():
    while True:
        expresion = input("Ingrese una expresión matemática (o 'exit' para salir): ")

        if expresion.lower() == 'exit':
            print("¡Hasta luego!")
            break

        try:
            resultado = eval(expresion)
            print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Error al evaluar la expresión: {e}")

if __name__ == "__main__":
    calculadora()