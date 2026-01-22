# Código corto de Python que saluda y calcula algo

nombre = input("¿Cuál es tu nombre? ")
edad = int(input("¿Cuántos años tienes? "))

print(f"\n¡Hola {nombre}!")
print(f"El año que viene tendrás {edad + 1} años")

# Pequeña operación
if edad >= 18:
    print("Eres mayor de edad 🎉")
else:
    print("Eres menor de edad 👶")

# Bonus: una mini calculadora
print("\n--- Mini calculadora ---")
num1 = float(input("Dame un número: "))
num2 = float(input("Dame otro número: "))
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} * {num2} = {num1 * num2}")