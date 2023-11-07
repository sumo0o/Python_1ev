#Este programa lee una contraseña y devuelve si es válida o no, de acuerdo con
#los siguientes criterios:
# 1.Más de 8 carácteres
# 2.Al menos una letra mayúscula X
# 3.Al menos una letra minúscula X
# 4.Al menos un número
# 5.Al menos un carácter especial X
# 6.No tiene espacios en blanco
#FUNCIONES
def verificaLongitud(contraseña): #Verifica si la palabra tiene más de 8 caracteres
  longitud=len(contraseña)
  respuesta=True
  if(longitud<=8):
    respuesta=False
  return(respuesta)

def verificaMayusculas(contraseña):# Verifica si la palabra contiene al menos 1 mayúscula
  respuesta=False
  for cont in range(0,len(contraseña)):
    if(contraseña[cont].isupper()):
       respuesta=True
  return(respuesta)

def verificaMinusculas(contraseña):
  respuesta=False
  for cont in range(0,len(contraseña)):
    if(contraseña[cont].islower()):
      respuesta=True
    return(respuesta)

def verificaNumeros(contraseña):
  respuesta=False
  for cont in range(0,len(contraseña)):
    if(contraseña[cont].isnumeric()):
      respuesta=True
    return(respuesta)

def verificaCaracteresExtraños(contraseña):
# Verifica si contiene alguno de los siguientes caracteres
#! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _` { | } ~
  respuesta=False
  lista="!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
  for cont1 in range(0,len(contraseña)): #La variable cont1 repasa las letras de la contraseña
    for cont2 in range(0,len(lista)):
      if(contraseña[cont]==lista[cont2]):
        respuesta=True
  return(respuesta)

  #Programa principal
  def verificaContraseña():
    contraseña=input("Introdu una contraseña: ")
    validez=0 #Defino una variable que me dice si es correcta
    #La doy por correcta mientras no se demuestre lo contrario
    if(verificaLongitud(contraseña)==True):
      validez=validez+1
      print("Longitud correcta")
    if(verificaMayusculas(contraseña)==True):
      validez=validez+1
      print
    if(verificaMinusculas(contraseña)==True):
      validez=validez+1
    if(verificaNumeros(contraseña)==True):
      validez=validez+1
    if(verificaCaracteresExtraños(contraseña)==True):
      validez=validez+1
    #SI validez cumple las cinco condiciones
    if(validez==5):
      print("Contraseña válida")
    else:
      print("Contraseña inválida")


  verificaLongitud(contraseña)
  verificaMayusculas(contraseña)
  verificaMinusculas(contraseña)
  verificaNumeros(contraseña)
  verificaCaracteresExtraños(contraseña)





verificaContraseña()
