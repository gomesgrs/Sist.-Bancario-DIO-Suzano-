import datetime

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)

    if opcao == "d":
        print("Você selecionou a função de Depósito")
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor: .2f}              Em: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n"

        else:
            print("Operação falhou. O valor informado não é válido.")

    elif opcao == "s":
        print("Você selecionou a função de Saque")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")

        elif excedeu_limite:
            print("O valor solicitado excede o limite permitido.")
        
        elif excedeu_saques:
            print("Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}                  Em: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n"
            numero_saques +=1

        else:
            print("O valor informado é invalido!")


    elif opcao == "e":
        print("Você selecionou a função de Extrato")
        print("\n-------------------- EXTRATO --------------------")
        print("Não foram realizadas movimentações na conta." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n------------------------------------------------")

    elif opcao == "q":
        print("Você selecionou a função Sair. Obrigado por utilizar nossos serviços. Até a próxima!")
        break
    
    else: 
        print("Você selecionou uma opção inválida. Por favor tente novamente.")
