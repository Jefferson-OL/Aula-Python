acesso = input("Qual seu nivel de acesso? ").upper()
if acesso !="ADM" and acesso !="USR" and acesso !="GUEST" and acesso !=(""):
   acesso = input("Não é um usuário valido, defina novamente: ")

sexo = input("Qual seu genêro sexual? HOMEM ou MULHER? ").upper()
if sexo !="HOMEM" and sexo !="MULHER":
    sexo = input("Resposta invalida, tente novamente: ").upper()

if acesso == "ADM" and sexo =="HOMEM":
    print("Olá Administrador!")
elif acesso == "ADM" and sexo=="MULHER":
    print("Olá Administradora!")

if acesso =="USR" and sexo=="HOMEM":
    print("Olá Usuário!")
elif acesso == "USR" and sexo=="MULHER":
    print("Olá Usuária!")

if acesso == (""): 
    print("Olá Desconhecido(a)!")
 

 






 

    


