
import os;
import sesion as se;


while True:
    def menu():

        print("*******Banco Federal CCO*******")
        print('1. Iniciar Sesion')


        opcion = int(input("Elija la opcion: "))
        os.system("cls")
        if opcion == 1:
            se.login()
            os.system("cls")
            
    menu()
    break

