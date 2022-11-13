import random

menu00 = "\n" + "*" * 10 + "Main Menu 00" + "*" * 10 + "\n" + "1)Items \n2)Purchases \n3)Customers \n4)Exit"
menu01 = "\n" + "*" * 10 + "Menu Item 01" + "*" * 10 + "\n" + "1)New Item\n2)Modity Item\n3)Find Items\n4)List Items\n5)Go back"
menu012 = "\n" + "*" * 10 + "Menu Modify Item 12" + "*" * 10 + "\n" + "1)Name\n2)Stock\n3)Price\n4)Show item\n5)Main Menu\n6)Go back"

menu013 = "\n" + "*" * 10 + "Menu Find Items 13" + "*" * 10 + "\n" + "1)Find item by id\n2)Find item by name\n3)Main menu\n4)Go back"
menu014 = "\n" + "*" * 10 + "Menu List Item 14" + "*" * 10 + "\n" + "1)List by id\n2)List by name\n3)List by Stock\n4)List 3 best selling items\n5)List 3 least sold items\n6)Main Menu\n7)Go back"

menu02 = "\n" + "*" * 10 + "Menu Purchases 02" + "*" * 10 + "\n" + "1)Find Purchase\n2)List Purchase\n3)New Purchase\n4)Go back"
menu022 = "\n" + "*" * 10 + "Menu Modify List Purchases 22" + "*" * 10 + "\n" + "1)List all purchases\n2)List that contain some item\n3)Go back\n4)Main menu"

menu03 = "\n" + "*" * 10 + "Menu Customers 03" + "*" * 10 + "\n" + "1)New Customer\n2)Find Customer\n3)Go back"
menu032 = "\n" + "*" * 10 + "Menu Find Customer 32" + "*" * 10 + "\n" + "1)Find by NIF\n2)Find by name\n3)Find top 3 highest spending customers\n4)Main Menu\n5)Go back"
menu0321 = "\n" + "*" * 10 + "Menu Show customer's purchases 321" + "*" * 10 + "\n" + "1)Show purchases\n2)Show detailed purchases\n3)Main menu\n4)Go back"

# Estructura de datos

dict_articulos = {4: {"nombre": "ASUS TUF GeForce RTX", "stock": 6, "precio": 1400},
                  2: {"nombre": "ASUS DUAL Radeon RX6600", "stock": 12, "precio": 294},
                  3: {"nombre": "Intel Core i7-13700K", "stock": 9, "precio": 530},
                  1: {"nombre": "Kingston Fury Beast 32GB", "stock": 10, "precio": 180},
                  10: {"nombre": "Corsair DC Cable Pro Kit", "stock": 20, "precio": 110},
                  11: {"nombre": "Gigabyte GC-TITAN RIDGE 2.0", "stock": 15, "precio": 81},
                  }

dict_compras = {"AA32E": {"fecha": 20201101, "articulos": {3: 1, 4: 1}},
                "AB37Z": {"fecha": 20201101, "articulos": {1: 1, 4: 1}},
                "CF13U": {"fecha": 20201101, "articulos": {1: 1, 3: 1}},
                "KL11T": {"fecha": 20201101, "articulos": {1: 3, 3: 2, 4: 2}},
                "ST234": {"fecha": 20191207, "articulos": {1: 1, 3: 1, 4: 1}},
                "NL345": {"fecha": 20181207, "articulos": {1: 1, 2: 1, 3: 1}},
                "SG345": {"fecha": 20190407, "articulos": {1: 1, 2: 1, 3: 1, 4: 3}},
                "SU798": {"fecha": 20210107, "articulos": {2: 2, 10: 3, 11: 1}}
                }

dict_clientes = {"34343434H": {"nombre": "Pedro", "telefono": "666994455"},
                 "78787878K": {"nombre": "Luis", "telefono": "666765432"},
                 "39292939S": {"nombre": "Jose Luis", "telefono": "666232211"},
                 "53423454C": {"nombre": "Lorenzo Lamas", "telefono": "666987578"},
                 "87654334T": {"nombre": "Arnau Soler", "telefono": "555443322"}
                 }

cliente_compra = {"34343434H": ["AA32E", "AB37Z", "SG345"],
                  "78787878K": ["CF13U", "KL11T"],
                  "39292939S": ["ST234"],
                  "53423454C": ["NL345"],
                  "87654334T": ["SU798"]
                  }

compra_cliente = {"AA32E": "34343434H",
                  "AB37Z": "34343434H",
                  "CF13U": "78787878K",
                  "KL11T": "78787878K",
                  "ST234": "39292939S",
                  "NL345": "53423454C",
                  "SG345": "34343434H",
                  "SU798": "87654334T"
                  }

#


menu_actual = 0  # valores posibles: 0, 1, 2, 11, 12, 111, 112 ... El valor -1 indica terminar.

while menu_actual >= 0:

    while menu_actual == 0:
        # Obtener opción correcta
        opcion_ok = False
        while not opcion_ok:
            print(menu00)
            opc = input(">Opcion: ")
            if not opc.isdigit():
                print("La opcion ha de ser numérica")
                input("Pulse una tecla para continuar...\n")
            else:
                opc = int(opc)
                if opc > 4 or opc < 1:
                    print("La opción ha de estar entre 1 y 4")
                    input("Pulse una tecla para continuar...\n")
                else:
                    opcion_ok = True


        if opc == 1:

            ##   1)Items

            menu_actual = 1

        elif opc == 2:

            ##   2)Purchases

            menu_actual = 2

        elif opc == 3:

            ###  3)Customers

            menu_actual = 3

        elif opc == 4:

            print(f"\nclosed...")
            menu_actual = -1

    ###  1)Items

    while menu_actual == 1:

        print(menu01)
        opc = input(">Opcion: ")
        if not opc.isdigit():
            print("La opcion ha de ser numérica")
            input("Pulse una tecla para continuar...\n")
        else:
            opc = int(opc)
            if opc > 5 or opc < 1:
                print("La opción ha de estar entre 1 y 5")
                input("Pulse una tecla para continuar...\n")
            else:
                if opc == 1:

                    ###  1)New item

                    menu_actual = 11

                elif opc == 2:

                    ###### 2)Modify item

                    flag0311 = True
                    id = input("ID of the item to modify: ")
                    while flag0311:
                        if id.isnumeric():
                            for u in dict_articulos:
                                if int(id) == u:
                                    flag0311 = False
                                    break
                            if flag0311 == True:
                                print("There's no item with ID : ", id)
                                input("Press any key to continue")
                                id = input("ID of the item to modify: ")
                        if not id.isnumeric():
                            print("ID of items are only numerics")
                            input("Press any key to continue")
                            id = input("ID of the item to modify: ")

                    cadena = ""
                    cadena += str("\nID").ljust(10) + str(id).rjust(30) + "\n" + \
                              str("Name").ljust(10) + str(dict_articulos[int(id)]["nombre"]).rjust(30) + "\n" + \
                              str("Stock").ljust(10) + str(dict_articulos[int(id)]["stock"]).rjust(30) + "\n" + \
                              str("Price").ljust(10) + str(dict_articulos[int(id)]["precio"]).rjust(30) + "\n"
                    print(cadena)
                    input("Press any key to continue")
                    menu_actual = 12
                    while menu_actual == 12:
                        print(menu012)
                        opc = input(">Opcion: ")
                        if not opc.isdigit():
                            print("La opcion ha de ser numérica")
                            input("Pulse una tecla para continuar...\n")
                        else:
                            opc = int(opc)
                            if opc > 6 or opc < 1:
                                print("La opción ha de estar entre 1 y 3")
                                input("Pulse una tecla para continuar...\n")
                            else:
                                if opc == 1:

                                    ##  1)modify by Name

                                    numbre = input("New name: ")

                                    cadena = ""
                                    cadena += str("ID").ljust(10) + str(id).rjust(30) + "\n" + \
                                              str("Name").ljust(10) + str(numbre).rjust(30) + "\n" + \
                                              str("Stock").ljust(10) + str(dict_articulos[int(id)]["stock"]).rjust(
                                        30) + "\n" + \
                                              str("Price").ljust(10) + str(dict_articulos[int(id)]["precio"]).rjust(
                                        30) + "\n"
                                    print("Save the item as? Y/y = yes:")
                                    print(cadena)
                                    pregunta = input("Answer: ")
                                    if pregunta == "Y" or pregunta == "y":
                                        dict_articulos[int(id)]["nombre"] = numbre
                                        menu_actual = 12
                                    else:
                                        menu_actual = 12
                                elif opc == 2:

                                    ##  2)modify by Stock

                                    stock = input("New Stock: ")

                                    cadena = ""
                                    cadena += str("ID").ljust(10) + str(id).rjust(30) + "\n" + \
                                              str("Name").ljust(10) + str(dict_articulos[int(id)]["nombre"]).rjust(
                                        30) + "\n" + \
                                              str("Stock").ljust(10) + str(stock).rjust(30) + "\n" + \
                                              str("Price").ljust(10) + str(dict_articulos[int(id)]["precio"]).rjust(
                                        30) + "\n"
                                    print("Save the item as? Y/y = yes:")
                                    print(cadena)
                                    pregunta = input("Answer: ")
                                    if pregunta == "Y" or pregunta == "y":
                                        dict_articulos[int(id)]["stock"] = int(stock)
                                        menu_actual = 12
                                    else:
                                        menu_actual = 12

                                elif opc == 3:

                                    ##  3)modify by Price

                                    price = input("New Price: ")
                                    cadena = ""
                                    cadena += str("ID").ljust(10) + str(id).rjust(30) + "\n" + \
                                              str("Name").ljust(10) + str(dict_articulos[int(id)]["nombre"]).rjust(
                                        30) + "\n" + \
                                              str("Stock").ljust(10) + str(dict_articulos[int(id)]["stock"]).rjust(
                                        30) + "\n" + \
                                              str("Price").ljust(10) + str(price).rjust(30) + "\n"
                                    print("Save the item as? Y/y = yes:")
                                    print(cadena)
                                    pregunta = input("Answer: ")
                                    if pregunta == "Y" or pregunta == "y":
                                        dict_articulos[int(id)]["precio"] = int(price)
                                        menu_actual = 12
                                    else:

                                        menu_actual = 12

                                elif opc == 4:

                                    ##  4)Show item

                                    cadena = ""
                                    cadena += str("ID").ljust(10) + str(id).rjust(30) + "\n" + \
                                              str("Name").ljust(10) + str(dict_articulos[int(id)]["nombre"]).rjust(
                                        30) + "\n" + \
                                              str("Stock").ljust(10) + str(dict_articulos[int(id)]["stock"]).rjust(
                                        30) + "\n" + \
                                              str("Price").ljust(10) + str(dict_articulos[int(id)]["precio"]).rjust(
                                        30) + "\n"
                                    print(cadena)
                                    input("Press any key to continue")
                                    menu_actual = 12
                                elif opc == 5:

                                    ## 5)Main Menu

                                    menu_actual = 0
                                elif opc == 6:

                                    ## 6)Go back

                                    menu_actual = 1
                elif opc == 3:

                    ## 3)Find item

                    menu_actual = 13

                elif opc == 4:

                    ##4)List items

                    menu_actual = 14

                elif opc == 5:

                    ###5)Go back

                    menu_actual = 0

    while menu_actual == 11:

        ##  1)New item

        flag0344 = True
        id = input("Id of the new item: ")
        while flag0344:
            if id.isnumeric():
                comprovar = 0
                for u in dict_articulos:
                    if int(id) == u:
                        comprovar += 1
                if comprovar != 0:
                    print("\nID : {} already exists".format(id))
                    input("Press any key to continue")
                    id = input("ID of the item to modify: ")
                if comprovar == 0:
                    flag0311 = False
                    break
            if not id.isnumeric():
                print("Incorrect ID")
                input("Press any key to continue")
                id = input("ID of the item to modify: ")

        print("\nId of the new item: {}\n".format(id))
        nombre = input("Item's name: ")
        stock = input("Items in stock: ")
        precio = input("Price of the new item: ")
        print("\nID: {}\nName: {}\nStock: {}\nPrice: {}".format(id, nombre, stock, precio))
        pregunta = input("Save the item as? Y/y = yes:")
        if pregunta == "Y" or pregunta == "y":
            dict_articulos.update({int(id): {"nombre": nombre, "stock": int(stock), "precio": int(precio)}})
            print("Item saved!!")
            input("\nPress any key to continue")

        else:
            print("Item not updated")
            input("\nPress any key to continue")

        menu_actual = 1

    while menu_actual == 13:

        ## 3)Find item

        print(menu013)
        opc = input("Opcion: ")
        if not opc.isdigit():
            print("La opcion ha de ser numérica")
            input("Pulse una tecla para continuar...\n")
        else:
            opc = int(opc)
            if opc > 4 or opc < 1:
                print("La opción ha de estar entre 1 y 3")
                input("Pulse una tecla para continuar...\n")
            else:
                if opc == 1:

                    # 1)Find item by id

                    idbuscar = int(input("Id to find: "))
                    print(idbuscar)
                    print("Items in Asian Shop Center")

                    cadena = "\nId".ljust(10) + "Name".ljust(30) + "Stock".ljust(20) + "Price".ljust(
                        5) + "\n" + "*" * 65 + "\n"
                    temp0411 = []
                    for u in dict_articulos:
                        temp0411.append(u)
                    cont2 = 0
                    for u in temp0411:
                        if u == idbuscar:
                            cadena = cadena + str(u).ljust(9) + dict_articulos[u]["nombre"].ljust(30) + str(
                                dict_articulos[u]["stock"]).ljust(20) + str(dict_articulos[u]["precio"]).ljust(5) + "\n"
                            cont2 += 1
                    if cont2 == 0:
                        cadena = cadena + str("There's not items with the string = " + str(idbuscar)).ljust(9) + "\n"
                        print(cadena)
                        input("Press any key to continue ")
                    else:
                        print(cadena)
                        input("Press any key to continue ")

                elif opc == 2:

                    # 2)Find item by name

                    usuario = input("What to look for?: ")
                    print(usuario)
                    print("Items in Asian Shop Center")

                    cadena = "\nId".ljust(10) + "Name".ljust(30) + "Stock".ljust(20) + "Price".ljust(
                        5) + "\n" + "*" * 65 + "\n"
                    temp0411 = []
                    for u in dict_articulos:
                        temp0411.append(dict_articulos[u]["nombre"])

                    ## Opcional "Sin importar mayusculas y minusculas en la busqueda"
                    for i in range(len(temp0411)):
                        temp0411[i] = temp0411[i].lower()

                    cont = 0
                    cont2 = 0
                    for u in dict_articulos:
                        if temp0411[cont].find(usuario.lower()) >= 0:
                            cadena = cadena + str(u).ljust(9) + dict_articulos[u]["nombre"].ljust(30) + str(
                                dict_articulos[u]["stock"]).ljust(20) + str(dict_articulos[u]["precio"]).ljust(5) + "\n"
                            cont2 += 1
                        cont += 1
                    if cont2 <= 0:
                        cadena = cadena + str("There's not items with the string = " + usuario).ljust(9) + "\n"
                        print(cadena)
                        input("Press any key to continue ")
                    else:
                        print(cadena)
                        input("Press any key to continue ")

                elif opc == 3:

                    ## 3)Main menu

                    menu_actual = 0

                elif opc == 4:

                    ## 4)Go back

                    menu_actual = 1

    while menu_actual == 14:

        ## 4)List items

        print(menu014)
        opc = input(">Opcion: ")
        if not opc.isdigit():
            print("La opcion ha de ser numérica")
            input("Pulse una tecla para continuar...\n")
        else:
            opc = int(opc)
            if opc > 7 or opc < 1:
                print("La opción ha de estar entre 1 y 3")
                input("Pulse una tecla para continuar...\n")
            else:

                if opc == 1:

                    # 1)List by id

                    temp0411 = []
                    for u in dict_articulos:
                        temp0411.append(u)
                    for i in range(len(temp0411) - 1):
                        for j in range(i + 1, len(temp0411)):
                            if temp0411[i] > temp0411[j]:
                                temp = temp0411[i]
                                temp0411[i] = temp0411[j]
                                temp0411[j] = temp
                    cadena = "\nId".ljust(10) + "Name".ljust(30) + "Stock".ljust(20) + "Price".ljust(
                        5) + "\n" + "*" * 65 + "\n"
                    for u in temp0411:
                        cadena = cadena + str(u).ljust(9) + dict_articulos[u]["nombre"].ljust(30) + \
                                 str(dict_articulos[u]["stock"]).ljust(20) + str(dict_articulos[u]["precio"]).ljust(
                            5) + "\n"
                    print(cadena)
                    input("Enter to continue")
                    menu_actual = 14




                elif opc == 2:

                    ## 2)List by name

                    temp0422 = []
                    for u in dict_articulos:
                        temp0422.append(dict_articulos[u]["nombre"])
                    for i in range(len(temp0422) - 1):
                        for j in range(i + 1, len(temp0422)):
                            if temp0422[i] > temp0422[j]:
                                temp = temp0422[i]
                                temp0422[i] = temp0422[j]
                                temp0422[j] = temp
                    cadena = "\nId".ljust(10) + "Name".ljust(30) + "stock".ljust(20) + "precio".ljust(
                        5) + "\n" + "*" * 75 + "\n"
                    for u in temp0422:
                        for v in dict_articulos:
                            if dict_articulos[v]["nombre"] == u:
                                cadena = cadena + str(v).ljust(10) + dict_articulos[v]["nombre"].ljust(30) + \
                                         str(dict_articulos[v]["stock"]).ljust(20) + str(
                                    dict_articulos[v]["precio"]).ljust(5) + "\n"
                                break
                    print(cadena)
                    input("Enter to continue")
                    menu_actual = 14

                elif opc == 3:

                    ## 3)List by stock

                    temp0422 = []
                    for u in dict_articulos:
                        temp0422.append(dict_articulos[u]["stock"])
                    for i in range(len(temp0422) - 1):
                        for j in range(i + 1, len(temp0422)):
                            if temp0422[i] > temp0422[j]:
                                temp = temp0422[i]
                                temp0422[i] = temp0422[j]
                                temp0422[j] = temp
                    cadena = "\nId".ljust(10) + "Name".ljust(30) + "stock".ljust(20) + "precio".ljust(
                        5) + "\n" + "*" * 75 + "\n"
                    for u in temp0422:
                        for v in dict_articulos:
                            if dict_articulos[v]["stock"] == u:
                                cadena = cadena + str(v).ljust(10) + dict_articulos[v]["nombre"].ljust(30) + \
                                         str(dict_articulos[v]["stock"]).ljust(20) + str(
                                    dict_articulos[v]["precio"]).ljust(5) + "\n"
                                break
                    print(cadena)
                    input("Enter to continue")
                    menu_actual = 14

                elif opc == 4:

                    ## 4)List 3 best selling items

                    temp0413 = {}
                    for clave in dict_articulos:
                        temp0413[clave] = 0

                    for u in dict_compras:
                        for clave, ventas in dict_compras[u]["articulos"].items():
                            temp0413[clave] += ventas

                    temp0422 = list(temp0413.keys())

                    for i in range(len(temp0422) - 1):
                        for j in range(len(temp0422) - 1 - i):
                            if temp0413[temp0422[j]] < temp0413[temp0422[j + 1]]:
                                temp = temp0422[j]
                                temp0422[j] = temp0422[j + 1]
                                temp0422[j + 1] = temp

                    cadena = "\nId".ljust(10) + "Name".ljust(35) + "stock".ljust(20) + "Price".ljust(
                        10) + "Sold out".ljust(5) + "\n" + "*" * 82 + "\n"

                    for i in range(3):
                        cadena = cadena + str(temp0422[i]).ljust(9) + dict_articulos[temp0422[i]]["nombre"].ljust(35) + \
                                 str(dict_articulos[temp0422[i]]["stock"]).ljust(20) + str(
                            dict_articulos[temp0422[i]]["precio"]).ljust(11) + \
                                 str(temp0413[temp0422[i]]).ljust(5) + "\n"
                    print(cadena)
                    input("Enter to continue")

                    menu_actual = 14

                elif opc == 5:

                    ## 5)List 3 least sold items

                    temp0413 = {}
                    for clave in dict_articulos:
                        temp0413[clave] = 0

                    for u in dict_compras:
                        for clave, ventas in dict_compras[u]["articulos"].items():
                            temp0413[clave] += ventas

                    temp0422 = list(temp0413.keys())

                    for i in range(len(temp0422) - 1):
                        for j in range(len(temp0422) - 1 - i):
                            if temp0413[temp0422[j]] > temp0413[temp0422[j + 1]]:
                                temp = temp0422[j]
                                temp0422[j] = temp0422[j + 1]
                                temp0422[j + 1] = temp

                    cadena = "\nId".ljust(10) + "Name".ljust(35) + "stock".ljust(20) + "Price".ljust(
                        10) + "Sold out".ljust(5) + "\n" + "*" * 82 + "\n"

                    for i in range(3):
                        cadena = cadena + str(temp0422[i]).ljust(9) + dict_articulos[temp0422[i]]["nombre"].ljust(35) + \
                                 str(dict_articulos[temp0422[i]]["stock"]).ljust(20) + str(
                            dict_articulos[temp0422[i]]["precio"]).ljust(11) + \
                                 str(temp0413[temp0422[i]]).ljust(5) + "\n"
                    print(cadena)
                    input("Enter to continue")

                    menu_actual = 14

                elif opc == 6:

                    ## 6)Main menu

                    menu_actual = 0

                elif opc == 7:

                    ## 7)Go back

                    menu_actual = 1

    while menu_actual == 2:

        ###  2)Purchases

        print(menu02)
        opc = input(">Opcion: ")
        if not opc.isdigit():
            print("La opcion ha de ser numérica")
            input("Pulse una tecla para continuar...\n")
        else:
            opc = int(opc)
            if opc > 4 or opc < 1:
                print("La opción ha de estar entre 1 y 3")
                input("Pulse una tecla para continuar...\n")
            else:
                if opc == 1:

                    ###    1)Find purchase

                    print("\nNo Implementado!!")
                    menu_actual = 2

                elif opc == 2:

                    ## 2)List Purchase

                    menu_actual = 22

                elif opc == 3:

                    ## 3)New Purchase

                    print("\nNo Implementado!!")
                    menu_actual = 2

                elif opc == 4:

                    ## 4)Go back

                    menu_actual = 0

    while menu_actual == 22:

        ## 2)List Purchase

        print(menu022)
        opc = input(">Opcion: ")
        if not opc.isdigit():
            print("La opcion ha de ser numérica")
            input("Pulse una tecla para continuar...\n")
        else:
            opc = int(opc)
            if opc > 4 or opc < 1:
                print("La opción ha de estar entre 1 y 4")
                input("Pulse una tecla para continuar...\n")
            else:
                if opc == 1:

                    ## 1)List all purchases

                    total = 0
                    listatotal = []

                    for u in dict_compras:
                        for clave, ventas in dict_compras[u]["articulos"].items():
                            total += (dict_articulos[clave]["precio"] * ventas)
                        listatotal.append(total)
                        total = 0

                    cadena = "\nID Compra".ljust(15) + "Cliente".ljust(30) + "Fecha".rjust(8) + "total_compras".rjust(
                        22) + "\n" + "*" * 74 + "\n"
                    cont = 0
                    for v in dict_compras:
                        cadena = cadena + str(v).ljust(14) + dict_clientes[compra_cliente[v]]["nombre"].ljust(30) + \
                                 str(dict_compras[v]["fecha"]).rjust(0) + str(listatotal[cont]).rjust(22) + "\n"
                        cont += 1
                    print(cadena)
                    input("Press any key to continue")

                if opc == 2:

                    ###  2)List purchases that contain some item

                    id = input("ID del artículo: ")
                    temp0413 = {}
                    for u in dict_compras:
                        for clave, ventas in dict_compras[u]["articulos"].items():
                            if int(id) == clave:
                                temp0413[u] = dict_compras[u]["articulos"]

                    print()
                    if len(temp0413) > 0:
                        print(f"Listamos compras del articulo  {id}")

                        total = 0
                        total2 = 0
                        listatotal = []
                        listatotal2 = []
                        for u in temp0413:
                            for clave, ventas in dict_compras[u]["articulos"].items():
                                total += (dict_articulos[clave]["precio"] * ventas)
                            listatotal2.append(total)
                            total = 0

                        for u in temp0413:
                            for clave, ventas in dict_compras[u]["articulos"].items():
                                total2 += (dict_articulos[clave]["precio"])
                                listatotal.append(total2)
                                total2 = 0

                        cadena = "\nID".ljust(10) + "Customer".ljust(15) + "ID item".ljust(10) + "Name item".ljust(
                            30) + "Amount".ljust(16) + "Price".ljust(16) + "\n" + "*" * 85 + "\n"
                        cont = 0
                        cont2 = 0

                        for cliente in temp0413:
                            cadena = cadena.strip(" ") + str(cliente).ljust(10) + \
                                     dict_clientes[compra_cliente[cliente]]["nombre"].ljust(15)
                            for datos in temp0413[cliente]:
                                cadena = cadena + str(datos).ljust(10) + str(dict_articulos[datos]["nombre"]).ljust(
                                    30) + str(temp0413[cliente][datos]).ljust(15) + str(listatotal[cont]).ljust(
                                    16) + "\n" + "   ".ljust(10) + "   ".ljust(15)
                                cont += 1
                            cadena = cadena.strip(" ") + "-" * 88 + "\n"
                            cadena = cadena + "Total".rjust(0) + " ".rjust(75) + str(listatotal2[cont2]).ljust(
                                0) + "\n\n\n"
                            cont2 += 1
                        print(cadena)
                        input("Press any key to continue")
                    else:
                        print(f"There is not item with ID:  {id}")
                        input("Press any key to continue")

                if opc == 3:
                    menu_actual = 2
                if opc == 4:
                    menu_actual = 0

    while menu_actual == 3:

        ## 3)Customers

        print(menu03)
        opc = input(">Opcion: ")
        if not opc.isdigit():
            print("La opcion ha de ser numérica")
            input("Pulse una tecla para continuar...\n")
        else:
            opc = int(opc)
            if opc > 3 or opc < 1:
                print("La opción ha de estar entre 1 y 3")
                input("Pulse una tecla para continuar...\n")
            else:
                if opc == 1:

                    ##### 3-1) New customer

                    lestrasDNI = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q",
                                  "V", "H", "L", "C", "K", "E"]

                    while True:
                        dni = input("Enter new NIF: ")
                        while True:
                            if not dni[0:7].isnumeric():
                                print("The first 8 characters of DNI are numbers")
                                input("Press any key to continue")
                                dni = input("Enter new NIF: ")
                            if len(dni) != 9 or not dni[0:7].isdigit() or not dni[8].isalpha():
                                print("Dni has to end with a letter")
                                input("Press any key to continue")
                                dni = input("Enter new NIF: ")
                            elif lestrasDNI[int(dni[0:8]) % 23].lower != dni[8].lower:
                                print("Dni has to end with a letter")
                                input("Press any key to continue")
                                dni = input("Enter new NIF: ")
                            else:
                                print("DNI is correct")
                                input("Press any key to continue")
                                break

                        nombre = input("Name of te new customer: ")
                        while True:
                            if not nombre.isalpha():
                                print("Incorrect name")
                                input("Press any key to continue")
                                nombre = input("Name of te new customer: ")
                            else:
                                break

                        telefono = input('TFN of the new customer: ')
                        while True:
                            if not len(telefono) == 9 or not telefono[0:8].isdigit():

                                print("Incorrect TFN")
                                input("Press any key to continue")
                                telefono = input("TFN of the new customer: ")
                            else:
                                break

                        print("Du you want to create the new customer? Y/y=yes:")
                        print("\nNIF: {}\nName: {}\nTFN: {}".format(dni, nombre, telefono))

                        pregunta = input("\nAnswer: ")
                        if pregunta == "Y" or pregunta == "y":
                            dict_clientes.update({str(dni): {"nombre": nombre, "telefono": telefono}})
                            print("New client created!!")
                            input("\nPress any key to continue")
                        else:
                            print("New client not updated")
                            input("\nPress any key to continue")

                        menu_actual = 3
                        break

                elif opc == 2:

                    ## Menu Find Customers
                    menu_actual = 32

                elif opc == 3:

                    ## 3)Go back

                    menu_actual = 0

    while menu_actual == 32:

        ##  3-2) Find customer

        print(menu032)
        opc = input(">Opcion: ")
        if not opc.isdigit():
            print("La opcion ha de ser numérica")
            input("Pulse una tecla para continuar...\n")
        else:
            opc = int(opc)
            if opc > 5 or opc < 1:
                print("La opción ha de estar entre 1 y 5")
                input("Pulse una tecla para continuar...\n")
            else:
                if opc == 1:

                    ## 1)Find by NIF

                    menu_actual = 321

                if opc == 2:

                    ### 2)Find by name

                    usuario = input("Name to search: ")

                    cadena = "\nNIF".ljust(16) + "Name".ljust(20) + "TFN".ljust(0) + "\n" + "*" * 44 + "\n"
                    temp0411 = []
                    for u in dict_clientes:
                        temp0411.append((dict_clientes[u]["nombre"]))

                    for i in range(len(temp0411)):
                        temp0411[i] = temp0411[i].lower().strip()

                    cont = 0
                    cont2 = 0
                    for u in dict_clientes:
                        if temp0411[cont].find(usuario.lower()) >= 0:
                            cadena = cadena + str(u).ljust(15) + dict_clientes[u]["nombre"].ljust(20) + str(
                                dict_clientes[u]["telefono"]).ljust(0) + "\n"
                            cont2 += 1
                        cont += 1

                    if cont2 <= 0:
                        cadena = cadena + str("There is no name containing = " + usuario).ljust(9) + "\n"
                        print(cadena)
                        input("Press any key to continue ")
                    else:
                        print(cadena)
                        input("Press any key to continue ")

                if opc == 3:

                    ### 3)Find top 3 highest spending customers

                    cadena = "\nCustomer" + "NIF".rjust(15) + "Total Purchases".rjust(37) + "\n" + "*" * 60
                    listacompras = {}
                    listaordenada = list(cliente_compra.keys())
                    for i in listaordenada:
                        total = 0
                        for j in cliente_compra[i]:
                            lista_llaves = list(dict_compras[j]["articulos"])

                            for k in lista_llaves:
                                total += dict_articulos[k]["precio"] * dict_compras[j]["articulos"][k]
                        listacompras[i] = total

                    listaordenada = list(listacompras.keys())
                    print(cadena)
                    for i in range(len(listaordenada) - 1):
                        for j in range(len(listaordenada) - 1 - i):
                            if listacompras[listaordenada[j]] < listacompras[listaordenada[j + 1]]:
                                temp = listaordenada[j]
                                listaordenada[j] = listaordenada[j + 1]
                                listaordenada[j + 1] = temp
                    for i in range(3):
                        print(dict_clientes[listaordenada[i]]["nombre"].ljust(10) + listaordenada[i].rjust(19) + str(
                            listacompras[listaordenada[i]]).rjust(31))

                    input("\nPress any key to continue ")

                if opc == 4:

                    ## 4)Main menu
                    menu_actual = 0

                if opc == 5:

                    ## 5)Go back
                    menu_actual = 3

    while menu_actual == 321:

        ###3-2-1) Encontrar por DNI

        nif = input("Introduce el NIF del cliente: ")
        while True:
            if nif in dict_clientes:
                print("")
                print("NIF".ljust(15) + ":", nif)
                for clave, valor in dict_clientes[nif].items():
                    print(clave.title().ljust(15) + ":", valor)
                input("\nPress any key to continue")
                break
            else:
                print("No existe!")
                nif = input("Introduce el NIF del cliente: ")


        flag777 = True
        while flag777 == True:

            # 3-2-1) menu show customer's purchases

            print(menu0321)
            opc = input(">Opcion: ")
            if not opc.isdigit():
                print("La opcion ha de ser numérica")
                input("Pulse una tecla para continuar...\n")
            else:
                opc = int(opc)
                if opc > 4 or opc < 1:
                    print("La opción ha de estar entre 1 y 4")
                    input("Pulse una tecla para continuar...\n")
                else:
                    if opc == 1:

                        ### 1)Show purchases

                        # 1) guardo las compras del cliente del diccionario de cliente compra
                        temp0455 = list(cliente_compra.keys())

                        conta = 0
                        for i in temp0455:

                            if nif == i:
                                conta += 1

                        if conta > 0:

                            lista_compras = cliente_compra[nif]
                            # cabecera
                            cadena = "\nId purchase".ljust(22) + "Date".ljust(15) + "Total purchase".ljust(
                                20) + "\n" + "*" * 50 + "\n"

                            # 2) recorro la lista de compras y accedo al valor para
                            # cada clave de compra
                            for compra in lista_compras:

                                # guardo el valor para esa clave compra
                                valor = dict_compras[compra]

                                # calcular el total de la venta
                                # 3) guardo el diccionario de articulos de esa compra
                                dicc_articulo_compra = valor["articulos"]

                                # variable que guarda el total de la suma de la compra
                                totalCompra = 0

                                # recorrer el diccionario de articulos de esa compra
                                for clave, cantidad in dicc_articulo_compra.items():
                                    # guardo el precio de ese articulo según la clave
                                    precioArticulo = dict_articulos[clave]["precio"]

                                    # sumo al total de la compra el precio del articulo por la cantidad comprada
                                    totalCompra = totalCompra + (precioArticulo * cantidad)

                                # accedemos al valor de la clave compra del diccionario de compras y
                                # de forma anidada al valor de la clave fecha del diccionario que hay como
                                # valor para la clave compra
                                cadena = cadena + str(compra).ljust(21) + str(valor["fecha"]).ljust(15) + str(
                                    totalCompra).ljust(20) + "\n"

                            # imprimo la informacion
                            print(cadena)
                            input("Press any key to continue")
                        else:
                            cadena = "\nId purchase".ljust(21) + "Date".ljust(15) + "Total purchase".ljust(20) \
                                     + "\n" + "*" * 50 + "\n\n" + f"The customer with NIF {nif} has not purchases" + "\n"
                            print(cadena)
                            input("\nPress any key to continue")

                    elif opc == 2:

                        ### 2)Show detailed purchases

                        cadena = ""
                        temp0455 = list(cliente_compra.keys())

                        conta = 0
                        for i in temp0455:

                            if nif == i:
                                conta += 1

                        if conta > 0:

                            # 1) guardo las compras del cliente del diccionario de cliente compra
                            lista_compras = cliente_compra[nif]

                            # 2) recorro la lista de compras y accedo al valor para
                            # cada clave de compra
                            for compra in lista_compras:

                                # guardo el valor para esa clave compra
                                valor = dict_compras[compra]

                                # calcular el total de la venta
                                # 3) guardo el diccionario de articulos de esa compra
                                dicc_articulo_compra = valor["articulos"]

                                # variable que guarda el total de la suma de la compra
                                totalCompra = 0

                                # cabecera
                                cadena = cadena + "\nId".ljust(20) + "Date".ljust(20) + "Items".ljust(
                                    40) + "Amount".ljust(20) + "Item's price".ljust(20) + "\n" + "*" * 111 + "\n"

                                # recorrer el diccionario de articulos de esa compra
                                for clave, cantidad in dicc_articulo_compra.items():
                                    # guardo el precio de ese articulo según la clave
                                    precioArticulo = dict_articulos[clave]["precio"]

                                    # sumo al total de la compra el precio del articulo por la cantidad comprada
                                    totalCompra = totalCompra + (precioArticulo * cantidad)

                                    # guardo el nombre de ese articulo
                                    nombre = dict_articulos[clave]["nombre"]

                                    # accedemos al valor de la clave compra del diccionario de compras y
                                    # de forma anidada al valor de la clave fecha del diccionario que hay como
                                    # valor para la clave compra
                                    cadena = cadena + str(compra).ljust(20) + str(valor["fecha"]).ljust(
                                        20) + nombre.ljust(40) + str(cantidad).ljust(20) + str(
                                        precioArticulo).ljust(20) + "\n"

                                cadena = cadena + "-" * 111
                                cadena = cadena + "\nTotal".ljust(100) + str(totalCompra) + "\n"
                                opc = 0
                            # imprimo la informacion
                            print(cadena)
                            input("\nPress any key to continue")
                        else:
                            cadena = cadena + "\nId".ljust(20) + "Date".ljust(20) + "Items".ljust(40) + "Amount".ljust(
                                20) + "Item's price".ljust(20) + \
                                     "\n" + "*" * 111 + "\n\n" + f"The customer with NIF {nif} has not purchases" + "\n"
                            print(cadena)
                            input("\nPress any key to continue")
                    elif opc == 3:

                        ###3) Go to Main menu

                        flag777 = False
                        menu_actual = 0


                    elif opc == 4:

                        ###4) Go back
                        flag777 = False
                        menu_actual = 32