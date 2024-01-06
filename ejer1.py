import os

class Cajero:
    def __init__(self):
        self.intentos_restantes = 3
        self.monto = 2000
        self.continuar = True
        self.menu()

    def contraseña(self):
        while self.intentos_restantes > 0:
            user_register = {
                "admin": "123"
            }
            user = input("Ingrese el usuario: ")
            password = input("Ingrese la contraseña: ")

            # Validar usuario y contraseña
            if user in user_register and password == user_register[user]:
                print("Inicio de sesión exitoso. ¡Bienvenido,", user, "!")
                os.system('cls' if os.name == 'nt' else 'clear')
                return True
            else:
                self.intentos_restantes -= 1
                print(f"Contraseña incorrecta. Le quedan {self.intentos_restantes} intentos.")
                if self.intentos_restantes == 0:
                    print("No puede realizar operaciones.")
                    self.continuar = False
                    return False

    def menu(self):
        if not self.contraseña():
            return

        opcion = 0
        while opcion != "4":
            print(""" 
                Bienvenido al cajero automático
                ****** Menú ******
                1- Depositar
                2- Retirar
                3- Ver saldo
                4- Salir 
                """)
            opcion = input("Su opción es: ")

            if self.continuar:
                if opcion == "1":
                    self.depositar()
                elif opcion == "2":
                    self.retiro()
                elif opcion == "3":
                    self.ver()
                elif opcion == "4":
                    print("Programa finalizado")
                else:
                    print("NO existe esa opción")
            else:
                if opcion == "4":
                    print("Programa finalizado")
                else:
                    print("Imposible realizar esa operación")

    def depositar(self):
        dep = int(input("Ingrese el monto a depositar: "))
        print(f"Usted ha depositado {dep}")
        print()
        print(f"Su nuevo saldo es {self.monto + dep}")
        self.monto += dep
    def retiro(self):
        retirar = int(input("¿Cuánto desea retirar? : "))
        print("Su monto actual es", self.monto)
        if self.monto >= retirar:
            print()
            print(f"Usted ha retirado: {retirar} , su nuevo monto es {self.monto - retirar}")
            self.monto -= retirar
        else:
            print("Imposible realizar el retiro, su monto es menor")

    def ver(self):
        print()
        print("Su saldo es:", self.monto)

app = Cajero()
