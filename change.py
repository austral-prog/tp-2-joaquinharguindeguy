def change():
    expense = 23.75
    money = 100
    vuelto = (money - expense)
    pesos = int(vuelto)
    centavos = (vuelto-pesos)
    centavos = int(centavos*100)
    print (f'Ingresar gasto\n{expense}\nDinero Recibido\n{money}\n\nVuelto\n\nPesos:\n{pesos}\nCentavos:\n{centavos}')

change()
