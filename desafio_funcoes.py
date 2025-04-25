from datetime import datetime
import textwrap

def menu():
    menu = """\n 
    ====================== MENU ======================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
            saldo += valor
            time_op = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"Depósito:  \tR$ {valor:.2f}      \t\tEm: {time_op}\n"
            print(f"\nDepósito realizado com sucesso!")

    else:
            print("Operação falhou. O valor informado não é válido.")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    
    if excedeu_saldo:
        print("Saldo insuficiente.")

    elif excedeu_limite:
        print("O valor solicitado excede o limite permitido.")
                
    elif excedeu_saques:
        print("Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        time_op = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        extrato += f"Saque:     \tR$ {valor:.2f}      \t\tEm: {time_op}\n"
        print(f"\nSaque realizado com sucesso!")
        numero_saques +=1

    else:
        print("O valor informado é invalido!")
        
    return saldo, extrato
    
def exibir_extrato(saldo, /, *, extrato):
    print("Você selecionou a função de Extrato")
    print("\n-------------------- EXTRATO --------------------")
    print("Não foram realizadas movimentações na conta." if not extrato else extrato)
    print(f"\nSaldo: \tR$ {saldo:.2f}")
    print("\n------------------------------------------------")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com este CPF!")
        return

    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/ sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco": endereco})

    print(f"Usuário criado com sucesso!")
                     
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontraro. Operação encerrada!")
    
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("="*100)
        print(textwrap.dedent(linha))
   
def main():
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            print("Você selecionou a função de Depósito")
            valor = float(input("Informe o valor do depósito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            print("Você selecionou a função de Saque")
            valor = float(input("Informe o valor do saque: "))
            
            saldo, extrato = sacar (
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            print("Você selecionou a função Sair. Obrigado por utilizar nossos serviços. Até a próxima!")
            break
        
        else: 
            print("Você selecionou uma opção inválida. Por favor tente novamente.")

main()