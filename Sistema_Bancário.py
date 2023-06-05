import os

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor :.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar(valor):
    global saldo, extrato, numero_saques
    if saldo >= valor and numero_saques < LIMITE_SAQUES and valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor :.2f}\n"
        numero_saques += 1
    else:
        print("Não foi possível realizar o saque.")


def exibir_extrato():
    global extrato
    global saldo
    print("Não foram realizadas movimentações." if not extrato else "...")
    print(f"Extrato: R${saldo:.2f}\n")
    print(f"{extrato}")


while True:
    print(
        """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """
    )

    opcao = input("=> ")

    if opcao == "d":
        os.system("cls")
        valor = float(input("Digite o valor a ser depositado: "))

        depositar(valor)
        print("Depósito realizado com sucesso.")

    elif opcao == "s":
        os.system("cls")
        valor = float(input("Digite o valor a ser sacado: "))
        sacar(valor)

    elif opcao == "e":
        os.system("cls")
        print("\n================ EXTRATO ================")
        exibir_extrato()
        print("==========================================")

    elif opcao == "q":

        os.system("cls")
        print("Programa encerrado.\n")
        break

    else:
        print("Opção inválida. Tente novamente.")
