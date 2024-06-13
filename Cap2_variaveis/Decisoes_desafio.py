nivel=input("Digite o nivel de acesso:") .upper()
if nivel=="ADM" or "USR":
    genero=input("Digite seu genero:") .upper()
    if nivel=="ADM":
        if genero=="FEMININO":
            print("Ola Administradora")
        else:
            print("Ola Administrador")
    elif genero!="FEMININO" and genero!="MASCULINO":
        print("Responda genero com MASCULINO ou FEMININO")
    else:
        if genero=="FEMININO":
            print("Ola usuaria")
        else:
            print("Ola usuario")

elif nivel=="GUEST":
    print("Ola visitante")
else:
    print("Ola desconhecido")
