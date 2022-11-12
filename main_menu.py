import random

menu00 = "\n"+"*"*10+"Main Menu 00"+"*"*10+"\n"+"1)Items \n2)Purchases \n3)Customers \n4)Exit"
menu01 = "\n"+"*"*10+"Menu Item 01"+"*"*10+"\n"+"1)New Item\n2)Modity Item\n3)Find Items\n4)List Items\n5)Go back"
menu012 = "\n"+"*"*10+"Menu Modify Item 12"+"*"*10+"\n"+"1)Name\n2)Stock\n3)Price\n4)Show item\n5)Main Menu\n6)Go back"

menu013 = "\n"+"*"*10+"Menu Find Items 13"+"*"*10+"\n"+"1)Find item by id\n2)Find item by name\n3)Main menu\n4)Go back"
menu014 = "\n"+"*"*10+"Menu List Item 14"+"*"*10+"\n"+"1)List by id\n2)List by name\n3)List by Stock\n4)List 3 best selling items\n5)List 3 least sold items\n6)Main Menu\n7)Go back"


menu02 = "\n"+"*"*10+"Menu Purchases 02"+"*"*10+"\n"+"1)Find Purchase\n2)List Purchase\n3)New Purchase\n4)Go back"
menu022 = "\n"+"*"*10+"Menu Modify List Purchases 22"+"*"*10+"\n"+"1)List all purchases\n2)List that contain some item\n3)Go back\n4)Main menu"

menu03 = "\n"+"*"*10+"Menu Customers 03"+"*"*10+"\n"+"1)New Customer\n2)Find Customer\n3)Go back"
menu032 = "\n"+"*"*10+"Menu Find Customer 32"+"*"*10+"\n"+"1)Find by NIF\n2)Find by name\n3)Find top 3 highest spending customers\n4)Main Menu\n5)Go back"
menu0321 = "\n"+"*"*10+"Menu Show customer's purchases 321"+"*"*10+"\n"+"1)Show purchases\n2)Show detailed purchases\n3)Main menu\n4)Go back"

# Estructura de datos

dict_articulos = {4: {"nombre": "ASUS TUF GeForce RTX", "stock": 6, "precio": 1400}, 
                  2: {"nombre": "ASUS DUAL Radeon RX6600", "stock": 12, "precio": 294},
                  3: {"nombre": "Intel Core i7-13700K", "stock": 9, "precio": 530},
                  1: {"nombre": "Kingston Fury Beast 32GB", "stock": 10, "precio": 180},
                  10: {"nombre": "Corsair DC Cable Pro Kit", "stock": 20, "precio": 110}, 
                  11: {"nombre": "Gigabyte GC-TITAN RIDGE 2.0", "stock": 15, "precio": 81},                 
                }


dict_compras = {"AA32E": {"fecha": 20201101, "articulos":{3:1,4:1}},
                "AB37Z": {"fecha": 20201101, "articulos":{1:1,4:1}}, 
                "CF13U": {"fecha": 20201101, "articulos":{1:1,3:1}}, 
                "KL11T": {"fecha": 20201101, "articulos":{1:3,3:2,4:2}}, 
                "ST234": {"fecha": 20191207, "articulos":{1:1,3:1,4:1}}, 
                "NL345": {"fecha": 20181207, "articulos":{1:1,2:1,3:1}}, 
                "SG345": {"fecha": 20190407, "articulos":{1:1,2:1,3:1,4:3}}, 
                "SU798": {"fecha": 20210107, "articulos":{2:2,10:3,11:1}}
                }

dict_clientes = {"34343434H": {"nombre": "Pedro", "telefono": "666994455"},
                 "78787878K": {"nombre": "Luis", "telefono": "666765432"}, 
                 "39292939S": {"nombre": "Jose Luis", "telefono": "666232211"}, 
                 "53423454C": {"nombre": "Lorenzo Lamas", "telefono": "666987578"}, 
                 "87654334T": {"nombre": "Arnau Soler", "telefono": "555443322"}                
                }

cliente_compra = {"34343434H": ["AA32E", "AB37Z","SG345"],
                  "78787878K": ["CF13U", "KL11T"], 
                  "39292939S": ["ST234"],
                  "53423454C": ["NL345"], 
                  "87654334T":["SU798"] 
                }

compra_cliente = {"AA32E": "34343434H",
                  "AB37Z": "34343434H",
                  "CF13U": "78787878K", 
                  "KL11T": "78787878K",
                  "ST234":"39292939S",
                  "NL345":"53423454C",
                  "SG345" :"34343434H",
                  "SU798":"87654334T"
                }


#



menu_actual = 0 # valores posibles: 0, 1, 2, 11, 12, 111, 112 ... El valor -1 indica terminar.

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
        # Tratar opción
        if opc == 1:
            menu_actual = 1
        elif opc == 2:
            menu_actual = 2
        elif opc == 3:
            menu_actual = 3
        elif opc == 4:
            print(f"\nclosed...")
            menu_actual = -1


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
                    menu_actual = 11
                elif opc == 2:
                    ########
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
                                        dict_articulos[int(id)]["stock"] = stock
                                        menu_actual = 12
                                    else:
                                        menu_actual = 12
                                elif opc == 3:
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
                                        dict_articulos[int(id)]["precio"] = price
                                        menu_actual = 12
                                    else:
                                        menu_actual = 12
                                elif opc == 4:
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
                                    menu_actual = 0
                                elif opc == 6:
                                    menu_actual = 1
                elif opc == 3:
                    menu_actual = 13
                elif opc == 4:
                    menu_actual = 14
                elif opc == 5:
                    menu_actual = 0

    while menu_actual == 11:

        ##Crear item

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

    while menu_actual == 3:
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
                    menu_actual = 31
                elif opc == 2:
                    menu_actual = 0
                elif opc == 3:
                    menu_actual = 0


    while menu_actual == 13:
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
                  #Buscar por id
                  idbuscar = int(input("Id to find: "))
                  print(idbuscar)
                  print("Items in Asian Shop Center")
                  
                  cadena = "\nId".ljust(10) + "Name".ljust(30) + "Stock".ljust(20) + "Price".ljust(5) +  "\n" + "*" * 65 + "\n"
                  temp0411 = []
                  for u in dict_articulos:
                      temp0411.append(u)

                  for u in temp0411:
                    if u == idbuscar:
                      cadena = cadena + str(u).ljust(9) + dict_articulos[u]["nombre"].ljust(30) + str(dict_articulos[u]["stock"]).ljust(20) + str(dict_articulos[u]["precio"]).ljust(5) + "\n"
                          
                  print(cadena)
                  input("Press any key to continue ")
                  
              elif opc == 2:
                  #Buscar por nombre
                  usuario = input("What to look for?: ")
                  print(usuario)
                  print("Items in Asian Shop Center")

                  cadena = "\nId".ljust(10) + "Name".ljust(30) + "Stock".ljust(20) + "Price".ljust(
                      5) + "\n" + "*" * 65 + "\n"
                  temp0411 = []
                  for u in dict_articulos:
                      temp0411.append(dict_articulos[u]["nombre"])
                  cont = 0
                  cont2=0
                  for u in dict_articulos:
                      if temp0411[cont].find(usuario) > 0:
                          cadena = cadena + str(u).ljust(9) + dict_articulos[u]["nombre"].ljust(30) + str(
                              dict_articulos[u]["stock"]).ljust(20) + str(dict_articulos[u]["precio"]).ljust(5) + "\n"
                          cont2+=1
                      cont += 1
                  if cont2 == 0:
                      cadena = cadena + str("There's not items with the string = " + usuario).ljust(9) + "\n"
                      print(cadena)
                      input("Press any key to continue ")
                  else:
                      print(cadena)
                      input("Press any key to continue ")

              elif opc == 3:
                  menu_actual = 0
              elif opc == 3:
                  menu_actual = 0
              elif opc == 4:
                  menu_actual = 0
                  
    while menu_actual == 14:
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

              #id

              if opc == 1:
                  temp0411 = []
                  for u in dict_articulos:
                      temp0411.append(u)
                  for i in range(len(temp0411) - 1):
                      for j in range(i + 1, len(temp0411)):
                          if temp0411[i] > temp0411[j]:
                              temp = temp0411[i]
                              temp0411[i] = temp0411[j]
                              temp0411[j] = temp
                  cadena = "\nId".ljust(10) + "Name".ljust(30) + "Stock".ljust(20) + "Price".ljust(5) +  "\n" + "*" * 65 + "\n"
                  for u in temp0411:
                      cadena = cadena + str(u).ljust(9) + dict_articulos[u]["nombre"].ljust(30) + \
                               str(dict_articulos[u]["stock"]).ljust(20) + str(dict_articulos[u]["precio"]).ljust(5) + "\n"
                  print(cadena)
                  input("Enter to continue")
                  menu_actual = 14

                  #name


              elif opc == 2:
                  temp0422 = []
                  for u in dict_articulos:
                      temp0422.append(dict_articulos[u]["nombre"])
                  for i in range(len(temp0422) - 1):
                      for j in range(i + 1, len(temp0422)):
                          if temp0422[i] > temp0422[j]:
                              temp = temp0422[i]
                              temp0422[i] = temp0422[j]
                              temp0422[j] = temp
                  cadena = "\nId".ljust(10) + "Name".ljust(30) + "stock".ljust(20) + "precio".ljust(5) +  "\n" + "*" * 75 + "\n"
                  for u in temp0422:
                      for v in dict_articulos:
                          if dict_articulos[v]["nombre"] == u:
                              cadena = cadena + str(v).ljust(10) + dict_articulos[v]["nombre"].ljust(30) + \
                                       str(dict_articulos[v]["stock"]).ljust(20) + str(dict_articulos[v]["precio"]).ljust(5) + "\n"
                              break
                  print(cadena)
                  input("Enter to continue")
                  menu_actual = 14

                  #stock

              elif opc == 3:
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


                #mas vendido
              elif opc == 4:
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

                  ##menos vendido
              elif opc == 5:
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
                  menu_actual = 0
              elif opc == 7:
                  menu_actual = 1


    while menu_actual == 2:

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
                    print("no implementado")
                    menu_actual=2
                elif opc == 2:
                    menu_actual = 22
                elif opc == 3:
                    print("no implementado")
                    menu_actual=2
                elif opc == 4:
                    menu_actual = 0


    while menu_actual == 22:
        print(menu022)
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
                if opc == 2:

                    id = input("ID del artículo: ")
                    temp0413 = {}
                    for u in dict_compras:
                        for clave, ventas in dict_compras[u]["articulos"].items():
                            if int(id) == clave:
                                temp0413[u] = dict_compras[u]["articulos"]

                    print()
                    if len(temp0413) > 0:
                        print(f"Listamos compras del articulo  {id}")
                        tempdni = {}
                        tempdni = list(cliente_compra.keys())

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
                            cadena = cadena + "   ".rjust(80) + str(listatotal2[cont2]).ljust(0) + "\n\n\n"
                            cont2 += 1
                        print(cadena)
                    else:
                        print(f"There is not item with ID:  {id}")

                if opc == 3:
                    menu_actual=2
                if opc == 4:
                    menu_actual=0