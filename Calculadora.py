
#Calculadora completa
def mostrarmenu():
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")

  respuesta = input("Ingrese su opción: ")
  return respuesta
  
def calculadora():
  respuesta=mostrarmenu()
  if respuesta=="1":
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    respuesta=n1+n2
    print("El resultado de la suma es: ", respuesta)
    
  elif respuesta=="2":
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    respuesta=n1-n2
    print("El resultado de la resta es: ", respuesta)
    
  elif respuesta=="3":
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    respuesta=n1*n2
    print("El resultado de la multiplicacion es: ", respuesta)
    
  elif respuesta=="4":
    n1=int(input("Ingrese el primer numero: "))
    n2=int(input("Ingrese el segundo numero: "))
    respuesta=n1/n2
    print("El resultado de la division es: ", respuesta)
    if(n2==0):
      print("No se puede dividir entre 0")
    
    
  else:
    print("Opcion invalida")
    
  return(respuesta)
  
# Programa principal
calculadora()
