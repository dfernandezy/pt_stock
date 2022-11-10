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
                    menu_actual = 0
                elif opc == 2:
                    menu_actual = 12
                elif opc == 3:
                    menu_actual = 13
                elif opc == 4:
                    menu_actual = 14
                elif opc == 5:
                    menu_actual = 0
                    
                    
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
                    menu_actual = 21
                elif opc == 2:
                    menu_actual = 22
                elif opc == 4:
                    menu_actual = 0

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

    while menu_actual == 4:
        print("Okay")
        break



      
    while menu_actual == 13:
      print(menu013)
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
                
                  usuario = int(input("Introduce el elemento a buscar: "))
                  print("ID to find: ")
                  print(usuario)
                  print("Items in Asian Shop Center")
                  
                  cadena = "\nId".ljust(10) + "Name".ljust(30) + "Stock".ljust(20) + "Price".ljust(5) +  "\n" + "*" * 65 + "\n"
                  temp0411 = []
                  for u in dict_articulos:
                      temp0411.append(u)

                  for u in temp0411:
                    if u == usuario:
                      cadena = cadena + str(u).ljust(9) + dict_articulos[u]["nombre"].ljust(30) + str(dict_articulos[u]["stock"]).ljust(20) + str(dict_articulos[u]["precio"]).ljust(5) + "\n"
                          
                  print(cadena)
                  input("Press any key to continue ")
                  
              elif opc == 2:
                  print("Introduzca el artículo que desee buscar por NOMBRE: ")
                  input("")
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
                  print(temp0413)

                  temp0422 = list(temp0413.keys())

                  for i in range(len(temp0422) - 1):
                      for j in range(len(temp0422) - 1 - i):
                          if temp0413[temp0422[j]] < temp0413[temp0422[j + 1]]:
                              temp = temp0422[j]
                              temp0422[j] = temp0422[j + 1]
                              temp0422[j + 1] = temp
                  print(temp0422)
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
                  print(temp0413)

                  temp0422 = list(temp0413.keys())

                  for i in range(len(temp0422) - 1):
                      for j in range(len(temp0422) - 1 - i):
                          if temp0413[temp0422[j]] > temp0413[temp0422[j + 1]]:
                              temp = temp0422[j]
                              temp0422[j] = temp0422[j + 1]
                              temp0422[j + 1] = temp
                  print(temp0422)
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
              
