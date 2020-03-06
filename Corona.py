nome = input("Qual nome do paciente?")
idade = int(input("Qual a idade?"))

doenca = input("Tem alguma doença (sim ou não)?").upper ()

if doenca!= "SIM" and doenca!= "NÃO":
    doenca = input("Entre somente com sim ou não:").upper()

if idade <15 or idade> 60:
    print("Tem risco vá para o hospital")

if doenca == "SIM":
     print("Atendimento prioritário") 
else:
    print("Acesse a fila normal")

