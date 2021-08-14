answer=("1")
while answer==("1"):
    answer= input ("Bienvenido, precione 1 para continuar o preciona 2 para salir ")
    print ("Iniciemos")
    
    a = int(answer)
    if  (a == 1):
        numero= int(input("Escriba un número"))
        porcentaje = numero * 0.15
        resultado= numero - porcentaje
        
        print ("Su resultado es ")
        print (resultado)
        
    else:
        print ("Adios")
