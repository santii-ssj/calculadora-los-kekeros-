

def sumar(a, b):
    resultado = a + b
    print("El resultado de la suma es:", resultado)


def restar(a, b):
    resultado = a - b
    print("El resultado de la resta es:", resultado)

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))


print("1. Sumar")
print("2. Restar")

opcion = input("Elige una opción (1 o 2): ")


if opcion == "1":
    sumar(num1, num2)

elif opcion == "2":
    restar(num1, num2)

else:
    print("Opción inválida")


