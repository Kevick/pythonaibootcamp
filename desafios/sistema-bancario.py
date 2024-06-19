"""
Sistema Bancário desenvolvido em Python para o bootcamp da dio!
"""

menu = """
        [d] DEPOSITAR
        [s] SACAR
        [e] EXTRATO BANCÁRIO
        [q] SAIR

Escolha uma opção: """
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar():
    global saldo, extrato
    deposito = int(input("Insira o valor para depósito: "))
    if deposito < 1:
        print("O valor minimo para depósito é de: R$1.00!")
    else: 
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print(f"Tudo certo com seu depósito!\n Valor depositado: R$ {deposito:.2f}\n Novo saldo: R$ {saldo:.2f}")


def sacar():
    global saldo, limite, extrato, numero_saques, LIMITE_SAQUES
    saque = int(input("Insira o valor para saque: "))
    if saldo < 1:
        print(f"Você não pode realizar um saque pois seu saldo é de R$ {saldo}")
    if numero_saques >= LIMITE_SAQUES:
        print(f"Você atingiu o limite de saque diário que é de {LIMITE_SAQUES} saques")
    elif saque > limite:
        print(f"O seu limite por saque é de R$ {limite:.2f}")
    elif saque > saldo:
        print(f"Você não pode realizar um saque pois seu saldo é de R$ {saldo:.2f} e o valor de saque foi R$ {saque:.2f}")
    else:
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        numero_saques += 1
        print(f"Tudo certo com seu saque!\n Valor sacado: R$ {saque:.2f}\n Novo saldo após saque: R$ {saldo:.2f}")

def exibir_extrato():
    global saldo, extrato
    if not extrato:
        print(f"Não foram realizadas movimentações. \nSeu saldo atual é de R$ {saldo:.2f}")
    else:
        print("\n---------- EXTRATO ----------")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")


while True:
    opcao = input(menu)
    if opcao == "d":
        depositar()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        exibir_extrato()
    elif opcao == "q":
        break
    else:
        print("Opção Inválida, por favor selecione novamente a operação desejada.")