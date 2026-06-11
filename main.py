def ejecutar_operacion(nombre_modulo, nombre_funcion, a, b):
    try:
        modulo = __import__(nombre_modulo)
        funcion = getattr(modulo, nombre_funcion)

        resultado = funcion(a, b)

        print(f"{nombre_funcion}({a}, {b}) = {resultado}")

    except ImportError:
        print(f"{nombre_funcion}: módulo '{nombre_modulo}.py' no encontrado")

    except AttributeError:
        print(f"{nombre_funcion}: función no encontrada")

    except Exception as e:
        print(f"{nombre_funcion}: error -> {e}")


print("=== CALCULADORA DEL EQUIPO ===")
print()

ejecutar_operacion("suma", "sumar", 10, 5)
ejecutar_operacion("resta", "restar", 10, 5)
ejecutar_operacion("multiplicacion", "multiplicar", 10, 5)
ejecutar_operacion("division", "dividir", 10, 5)
