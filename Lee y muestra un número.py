#
print("Hola, bienvenido al banco de Occidente")

cuenta1 = 1000000
cuenta2 = 500000

menu = 0

while menu != 3:
    print("\nOPCIONES")
    print("1. Retirar")
    print("2. Depositar")
    print("3. Salir del menú")
    
    print("\nSaldo cuenta 1:", cuenta1)
    print("Saldo cuenta 2:", cuenta2)
    
    menu = int(input("\n¿Qué deseas realizar hoy?: "))
    
    # retirar 
    if menu == 1:
        elegir = int(input("¿De qué cuenta deseas retirar? (1 o 2): "))
        valor = float(input("Monto a retirar: "))
        
        impuesto = valor * 0.004
        total_cobrado = valor + impuesto
        
        # Bloque cuenta 1
        if elegir == 1:
            if cuenta1 >= total_cobrado:
                cuenta1 -= total_cobrado
                print("Retiro exitoso. Se cobró el 4x1000.")
            else:
                print("Ups... No te alcanza en la cuenta 1")
        
        # Bloque cuenta 2
        elif elegir == 2:
            if cuenta2 >= total_cobrado:
                cuenta2 -= total_cobrado
                print("Retiro exitoso. Se cobró el 4x1000.")
            else:
                print("Ups... No te alcanza en la cuenta 2")
        
        else:
            print("no puedes hacer este movimiento")
    
    # depositar
    elif menu == 2:
        elegir = int(input("¿A qué cuenta deseas depositar? (1 o 2): "))
        valor = float(input("Monto a depositar: "))
        
        if elegir == 1:
            cuenta1 += valor
            print("Depósito exitoso en cuenta 1")
        
        elif elegir == 2:
            cuenta2 += valor
            print("Depósito exitoso en cuenta 2")
        
        else:
            print("error debes ingresar un valor valido a depositar")
    
    # salir del sistema
    elif menu == 3:
        print("Hasta luego, espero verte pronto...")
    
    else:
        print("invalido")