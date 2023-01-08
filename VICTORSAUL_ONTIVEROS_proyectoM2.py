#Programa que genera una contraseña de 8 caracteres a partir de 1 palabra dada por el usuario

palabra = input("introduce la palabra: ")

#si la palabra es de menos de 4 caracteres, se rellena con X

if len(palabra) <4:
  palabra = "X" + palabra
#Se genera contraseña
contraseña = palabra [0] 
print("la contraseña es: ", contraseña)

#se solicita contraseña al usuario
#Si la contraseña es de menos caracteres se informa cuantos caracteres faltan
#Si la contraseña excede los 8 caracteres se informa cuantos caracteres sobran
#si la contraseña es correcta, se informa que es correcta

contraseña_usuario = input("introduce la contraseña: ") #se solicita la contraseña al usuario
if len(contraseña_usuario) < len(contraseña):
  print("Faltan", len(contraseña)- len(contraseña_usuario), "caracteres")
elif len(contraseña_usuario) > len(contraseña):
  print("Sobran", len(contraseña_usuario)- len(contraseña), "caracteres")
elif contraseña_usuario == contraseña: 
  print("contraseña correcta")
else:
  print("contraseña incorrecta")    