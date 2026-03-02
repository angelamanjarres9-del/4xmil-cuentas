# BANCO.
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
    
    # menu o opciones posibles
    if menu == 1:
        elegir = int(input("¿De qué cuenta deseas retirar? (1 o 2): "))
        valor = float(input("Monto a retirar: "))
        
        impuesto = valor * 0.004
        
        # bloque cuenta 1
        if elegir == 1:
            if cuenta1 >= valor + impuesto:
                cuenta1 -= (valor + impuesto)
                print("Retiro exitoso. Se cobró el 4x1000")
            
            elif cuenta1 >= valor and cuenta2 >= impuesto:
                cuenta1 -= valor
                cuenta2 -= impuesto
                print("Retiro exitoso, recuerda que el 4x1000 fue prestado por cuenta 2 ")
            
            else:
                print("No hay saldo suficiente ")
        
        # bloque cuenta 2
        elif elegir == 2:
            if cuenta2 >= valor + impuesto:
                cuenta2 -= (valor + impuesto)
                print("Retiro exitoso, recuerda que el 4x1000 fue prestado por cuenta 1 ")
            
            elif cuenta2 >= valor and cuenta1 >= impuesto:
                cuenta2 -= valor
                cuenta1 -= impuesto
                print("Retiro exitoso. El 4x1000 fue prestado por cuenta 1")
            
            else:
                print("No hay saldo suficiente")
        
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
            print("no puedes hacer este movimiento")
    
    
    # ---------------- SALIR ----------------
    elif menu == 3:
        print("espero verte pronto... hasta luego")
    
    else:
        print("saliendo...")
