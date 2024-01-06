import os;


def money():
    while True:
        monedas_con_equivalencias = {
            "clp": 828.33,  
            "ars": 115.17,  
            "usd": 1,
            "eur": 0.81,
            "try": 14.16,   
            "gbp": 0.74     
}

        print("Monedas disponibles:")
        for moneda in monedas_con_equivalencias:
            print(moneda)

        nombre_moneda_origen = ""
        nombre_moneda_destino = ""
        while nombre_moneda_origen not in monedas_con_equivalencias:
            nombre_moneda_origen = input("Moneda origen: ")

        while nombre_moneda_destino not in monedas_con_equivalencias:
            nombre_moneda_destino = input("Moneda destino: ")


        cantidad = float(input(f"Ingresa la cantidad de {nombre_moneda_origen}: "))
        equivalencia_origen = monedas_con_equivalencias[nombre_moneda_origen]
        equivalencia_destino = monedas_con_equivalencias[nombre_moneda_destino]
        equivalencia = (equivalencia_destino/equivalencia_origen)*cantidad
        final = (equivalencia * 1)/100
        final = round(final, 2)
        equivalencia = equivalencia - final
        print(f"{cantidad:.2f} {nombre_moneda_origen} equivale a {equivalencia:.2f} {nombre_moneda_destino}.")
        print()
        print(final)
        
        desicion = input('1. Reniciar/ 2.Salir ')
        if desicion == "1":
             os.system('cls')
        else:
            print("Programa Finalizados")
            break
            

money() 

