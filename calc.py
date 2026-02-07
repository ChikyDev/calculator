'''Calculadora en python'''

import math

VERDE = "\033[92m" #Colores para resultados y errores
RESET = "\033[0m"
ROJO = "\033[91m"


while True: 

    print(' === CALCULADORA === ') #Menu de todas las opciones que da a elegir la calculadoa
    print('1. Suma ➕​')
    print('2. Resta ➖​')
    print('3. Multiplicacion ✖️​')
    print('4. Division ➗​')
    print('5. Raiz cuadrada √')
    print('6. Salir ❗​')

    eleccion = input('Escoje una de todas las opciones (1-6): ') #Aqui el usuario debera de elegir que tipo de operacion escoje

    if eleccion == '6': #Lo que esta indicando este if es que si el usuario pone 6, salga de la calculadora
        print('Saliendo de la calculadora...👋​')
        break

    if eleccion not in ['1', '2', '3', '4', '5', '6']:
        print('La opcion no es valida')
        continue
    
    #RAIZ CUADRADA

    if eleccion == '5':
        num1 = int(input('Introduce el numero: '))

        if num1 < 0:
            print(ROJO+  "No se puede calcular la raíz de un número negativo"+RESET)
            continue
        else:
            print(VERDE+ f'El resultado es: {math.sqrt(num1)}'+RESET)
            continue
        
        #OPERACIONES BASICAS
    num1 = int(input('Primer numero: ')) #las variables aparecen como numeros enteros
    num2 = int(input('Segundo numero: '))

    num1_decimal = float(num1) #el float es especialmente para las divisiones, que sea decimal la respuesta y por lo tanto evitar fallos de resultado
    num2_decimal = float(num2)

    if eleccion == '1': #Si el usuario responde con 1 se hara la operacion que aparece en el menu
        print(VERDE + f'El resultado es: {num1 + num2}' +RESET)
    elif eleccion == '2':
        print(VERDE + f'El resultado es: {num1 - num2}' +RESET)
    elif eleccion == '3':
        print(VERDE + f'El resultado es: {num1 * num2}' + RESET)
    elif eleccion == '4':
        if num2 == 0: #Indica que si el dividendo es 0 no se podra dividir
            print(ROJO+'No se puede dividir entre 0' +RESET)
        else: #Esto indica que si el resultado se puede dividir, se formalice la operación
            print(VERDE + f'El resultado es: {num1_decimal / num2_decimal}' +RESET)
       
    




