#01
usuarios = {"Marta","David","Elvira","Juan","Marcos"}

administradores = {"Juan","Marta"}

administradores.discard("Juan")
administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "Administrador")
    else:
        print(usuario, "Usuario")

#02
clases={}

caballero = {"vida": ,"ataque": ,"defensa": ,"alcance": ,}
guerrero = {"vida": ,"ataque": ,"defensa": ,"alcance": ,}
arquero = {"vida": ,"ataque": , "defensa": ,"alcance": ,}

