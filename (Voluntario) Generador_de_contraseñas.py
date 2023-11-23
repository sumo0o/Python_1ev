from random import choice #Esto lo hace aleatorio

def creador_auto_contraseñas(n):
  
  # Definir lista de caracteres
  caracteres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
                'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B',
                'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
                '4', '5', '6', '7', '8', '9', ".", "_", "!", "#", "$", "%", "&", "(",
                ")", "*", "+",]
  
    # Definir lista de contraseñas aleatorias
  random_password = ''.join(choice(caracteres) for i in range(n))
  return random_password



  #Para introducir el numero de caracteres 
n = int(input("Introduzca el número de caracteres: ")) 
print(creador_auto_contraseñas(n))  # Devuelve la contraseña elegida
