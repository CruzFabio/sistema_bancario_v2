# Criando a função do menu
def menu():
    menu = """
    |========== MENU ==========|

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Cadastro
        [5] Criar Conta
        [6] Listar Contas
        [0] Sair

    =>  """
    return int(input(menu))

# Criando a função depósito com parâmetro positional only
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
        print("\n🟢 Depósito realizado com sucesso!")
    else:
        print("\n🔴 Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato

# Criando a função saque com o uso de keyword only
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n🔴 Saldo insuficiente!")

    elif excedeu_limite:
        print("O valor do saque excede o limite!")

    elif excedeu_saques:
        print("Limite diário de saques excedido!")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n🟢 Saque realizado com sucesso!")
    
    else:
        print("\n🔴 Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# Criando a função extrato, os parâmetros serão em positional e keyword
def exibir_extrato(saldo, /, *, extrato):
    print("\n============ EXTRATO ============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\n>> Saldo disponível:\tR$ {saldo:.2f}")
    print("==================================")

def cadastrar_usuario(usuarios):
    print("\n============ CADASTRO ============")
    cpf = input("Informe o CPF (apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n🟡 Usuário já cadastrado no sistema!")
        return
    
    nome = input("Nome: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/UF): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco":endereco})

    print("\n🟢 Cadastro realizado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    print("\n============ NOVA CONTA ============")
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n 🟢 Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("\n🔴 Usuário não cadastrado!")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(linha)

# Criando uma função para fazer a chamada do código
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == 1: #depositar
            print("\n============ DEPÓSITO ============")
            valor = float(input("\nInforme o valor do depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == 2: #sacar
            print("\n============ SAQUE ============")
            valor = float(input("\nQual valor deseja sacar R$ "))

            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == 3: #extrato
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == 4: #cadastro de usuarios
            cadastrar_usuario(usuarios)

        elif opcao == 5: #criar conta
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA,numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == 6: #listar contas
            listar_contas(contas)

        elif opcao == 0: #sair
            break
        else:
            print("\n🔴 Opçâo Inválida, por favor selecione uma opção válida.")

main()