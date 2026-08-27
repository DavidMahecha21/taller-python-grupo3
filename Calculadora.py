import diviision as dv
import Suma as sm

while True:
    print("\n--- Calculadora Básica ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
    if(opcion == "1"):
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        
        print(sm.suma(num1, num2))
    if(opcion == "4"):
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        
        print(dv.division(num1, num2))
    