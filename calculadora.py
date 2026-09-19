def calculadora():
    print("================================")
    print("     CALCULADORA BÁSICA")
    print("================================")

    continuar = True

    while continuar:
        try:
            # Pedir los números
            num1 = float(input("\nIngresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            # Mostrar el menú
            print("\nSelecciona una operación:")
            print("1. Suma (+)")
            print("2. Resta (-)")
            print("3. Multiplicación (*)")
            print("4. División (/)")
            opcion = input("Opción: ")

            # Realizar la operación
            if opcion == "1":
                print(f"\nResultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == "2":
                print(f"\nResultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == "3":
                print(f"\nResultado: {num1} * {num2} = {num1 * num2}")
            elif opcion == "4":
                if num2 == 0:
                    print("\nError: No se puede dividir entre cero.")
                else:
                    print(f"\nResultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("\nOpción no válida.")
                continue  # vuelve a empezar sin preguntar si continuar

            # Preguntar si desea continuar
            respuesta = input("\n¿Deseas hacer otra operación? (s/n): ").lower()
            if respuesta != "s":
                continuar = False

        except ValueError:
            print("\nError: Debes ingresar un número válido.")

    print("\n¡Gracias por usar la calculadora!")


# Ejecutar el programa
if __name__ == "__main__":
    calculadora()
    