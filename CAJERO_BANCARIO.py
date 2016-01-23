#SIMULADOR DE CAJERO BANCARIO
#Creado por Edil de los Santos
balance = 49900
retiro_max = 50000
retiro_min = 200
print "Bienvenido.  "
print "Que desea realizar el dia de hoy? "
eleccion_usuario = input("Digite (1) si desea Consultar. Digite (2) si desea Retirar: ")
if eleccion_usuario == 1:
	print ""
        print "Su balance disponible es de: " + str(balance)
        print "Si desea realizar retiro. Retire la tarjeta e intente de nuevo. "   
    
#-------------------------------------------------------------------------------------------------------------------      
elif eleccion_usuario == 2:
        def eleccion_retiro(x,y):
                eleccion = input("Digite monto a retirar: ")
                intento_retiro = 3
                if eleccion > retiro_max:
                        while eleccion > retiro_max:
                                print "Fondo Insuficiente"
                                print "Su balance disponible es de: " + str(retiro_max)
                                intento_retiro -= 1
                                print "Le queda " + str(intento_retiro) + " intentos."
                                eleccion = input("Digite monto a retirar: ")
                                if intento_retiro == 1:
                                        print "Agoto sus intentos. Retire su tarjeta e intente de nuevo."
                                        break
                                elif eleccion >= retiro_min and eleccion <= retiro_max:
                                        print "Usted desea retirar " + str(eleccion) + " pesos."
                                        confirmar_monto = input("Digite (1) para confirmar o (2) para Salir: ")
                                        if confirmar_monto == 1:
                                                print "Retire su dinero. Gracias por preferirnos."
                                        elif confirmar_monto == 2:
                                                print "Transaccion abortada."
                                        else:
                                                print "Eleccion incorrecta. Retire su tarjeta e intente de nuevo: "
                                else:
                                        print "Este cajero no admite monto menor a 200. "       
#-------------------------------------------------------------------------------------------------------------------
                                        
                elif eleccion >= retiro_min or eleccion <= retiro_max:
                        print "Usted desea retirar " + str(eleccion) + " pesos."
                        confirmar_monto = input("Digite (1) para confirmar o (2) para Salir: ")
                        if confirmar_monto == 1:
                                print "Retire su dinero. Gracias por preferirnos."
                        elif confirmar_monto == 2:
                                print "Transaccion abortada."
                        else:
                                print "Eleccion incorrecta. Retire su tarjeta e intente de nuevo: "
                else:
                        print "Este cajero no admite monto menor a 200. "          
        eleccion_retiro(1,2)
else:
        print "Eleccion incorrecta. Retire su tarjeta e intente de nuevo. "
raw_input()

