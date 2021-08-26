import string
import random
import sys 
from palabras import pal 
from visual   import visual_consola


#########################################################################
#La siguiente funciion tomara los titulos de los conceptos para validarlos   
def get_con_til(listaC):
    listaC = random.choice(listaC)

    while '-' in listaC or '.' in listaC:
        conceptos = random.choice(conceptos)

    return conceptos.upper()     

#########################################################################
#La siguiente funciion tomara los titulos de los conceptos para validarlos    
def get_val_pal(pal):
    pal =  random.choice(pal)

    while '-' in pal or ' ' in pal: 
        pal = random.choice(pal)
        
    return pal.upper()

#########################################################################
#Menu del juego para interactuar mas facil con el usuario 
    #####    def menu():
        
    #####    print("***************Selecciona una Opcion*********************")
    #####    print("1. Game") #Play game
    #####    print("2.")      #Preparar Juego por medio del profesor
    #####    print("3.")      #Resultados
    #####    print("4. Salir") #Salir del sistema

    #####    while True:
    #####        menu()
    #####        opMenu =  input("Ingresa el numero de la Opcion :")
    #####        
    #####        if opMenu ==1:
    #####            print("1.")
    #####            game()
    #####            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
    #####        elif opMenu ==2:
    #####            print("2.")
    #####            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
    #####        elif opMenu ==3:
    #####            print("3.")
    #####            input("Has pulsado la opción 3...\npulsa una tecla para continuar")        
    #####        elif opMenu ==4:
    #####            print("4.")
    #####            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
    #####            break
    #####        else:
    #####            print("")
    #####            input("No has pulsado ninguna opcion correcta")
    #####
    #####    if __name__ == '__main__':
    #####        menu() # se pelo esta mierda


#########################################################################
def game():

    quemados =["uno","dos","tres","Cuatro"]

    palabra = ""
    pal_ = get_val_pal(pal)    #palabra
    #pal_ = get_con_til(listaC)
    let = set(pal_)            #Letras de la palabra
    abc = set(string.ascii_uppercase) #abecedario  ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' / debemos de remplazar esto por una lista de titulos de conceptos
    usu = set(palabra) #Letras adiviinadas por el estudiante

    vid = 7 #Tenemos como predeterminado 7 intentos

    #Tomando la entrada del usuaro
    while len(let) > 0 and  vid > 0:
        #Letras usando el usuario ,  mostramos las vidas y el acceso a las letras usadas
        print('Te quedan vidas', vid , 'has usado estas palabras:',''.join(usu))

        #Lista de palabras
        #antes si la palabra usada por el usuario esta sino no esta , en la palabra 
        pal_list = [letter if letter in usu else "-" for letter in pal]
        print(visual_consola[vid])
        print("Palabra actual:",''.join(pal_list))

        user =  input("Adivina una palabra :").upper()
        if user in abc - usu:
            usu.add(user)
            if user in let:
                let.remove(user)
                print("")

            else:
                vid =  vid - 1 #Quita la vida cada vez que se equivoque
                print("\n usado por ti:",usu,"no es la palabra") 
                
        elif user in usu:
            print("\n Ya usaste esa palabra. Adivina otra palabra")
        
        else:
            print("\n No  es valida la palabra")

      #Llega al final cuando encuentra la palabra o pierde las vidas  
    if vid == 0:
        print(visual_consola[vid])
        print("Has perido perdon, La palabra era", pal)

    else:
        print("YEEES boy , has completado corrctamente el juego", pal ,":::",usu, "!!!!!!!!")
#########################################################################
if __name__ == "__main__":
     game()     

