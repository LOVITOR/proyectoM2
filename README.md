#  Primero  solicitamos al programa colocar una palabra  que será la contraseña
palabra = input("introduce la palabra")

#si la palabra tiene menos de 4 caracteres se rellena con una letra X 

if len(palabra) < 4
#generamos la contraseña 
contraseña = palabra [0]
print("la contraseña es: ", contraseña)
#solicitamos la contraseña al usuario
#si la contraeña tiene menos de 4 caracteres de informa cuantos hacen falta, al igual que si tiene mas de 8 se informa cuantos sobran 
#se imprime en pantalla si la contraseña es correcta o incorrecta

contraseña_usuario =input("introduce la contraseña: ")
if len(contraseña_usuario) < len(contraseña): 
print("Faltan", len(contraseña) - len(contraseña_usuario), "caracteres")
elif len (contraseña_ususario) > len (contraseña):
print("Sobran", len(contraseña_usuario) - len(contraseña), "caracteres")
print("contraseña incorrecta")

