import datetime

menu = """

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
LIMITE_DIARIO = 10
numero_transacoes = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        excedeu_transacoes = numero_transacoes >= LIMITE_DIARIO
        
        if excedeu_transacoes:
            print("Operação falhou! Limite de 10 transacoes diarias.")

        if valor > 0:
            saldo += valor
            numero_transacoes += 1
            data = datetime.datetime.now()
            data = data.strftime("%d/%m/%Y %H:%M:%s")
            extrato += f"Depósito: R$ {valor:.2f} no dia {data}d\n" 

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        excedeu_transacoes = numero_transacoes >= LIMITE_DIARIO

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif excedeu_transacoes:
            print("Operação falhou! Limite de 10 transacoes diarias.")


        elif valor > 0:
            saldo -= valor
            data = datetime.datetime.now()
            data = data.strftime("%d/%m/%Y %H:%M:%s")
            extrato += f"Saque: R$ {valor:.2f} dno dia {data}\n "
            numero_transacoes += 1
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
