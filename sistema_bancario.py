"""
Objetivo: criar um sistema bancário com operações de sacar, depositar, e visualizar extrato

Operação de depósito
Todos os depósitos devem ser armazenadas em uma variável e exibir na tela a operação de extrato e todos depósitos devem ser positivos.

O sistema só pode permitir 3 saques diários com limite de R$500 em cada saque. Caso o usuário não estiver o saldo em conta o sistema deve exibir
uma mensagem que não é possível sacar o dinheiro por falta de saldo. Todos saques devem ser armazenados em uma variável e e exibidos na operação
 de extrato

Operação de extrato deve mostrar todos depósitos e saques realizados na conta e deve exibir o saldo atual da conta
"""
linha = "==================================="

menu = """
========== LegendaryBank ==========

                MENU
        Bem-Vindo de volta!

Qual operação você deseja efetuar?
    [0] Depósito
    [1] Sacar
    [2] Extrato
    [3] Sair do sistema
===================================
"""

tela_deposito = """
========== LegendaryBank ==========

        OPERAÇÃO DE DEPÓSITO

"""

tela_saque = """
========== LegendaryBank ==========

         OPERAÇÃO DE SAQUE
"""

tela_extrato = """
========== LegendaryBank ==========

             EXTRATO
"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
SAQUE_LIMITE = 3


while True:

    opcao = input(menu)
    if opcao == "0":
        print(tela_deposito) 
        valor_dep = float(input("Informe o valor do depósito: "))
        
        if valor_dep > 0:
            saldo += valor_dep
            print(f"O seu saldo é de R$: {saldo:.2f}\n\n" + linha)
            extrato += f"Depósito: R$ {valor_dep:.2f}\n"

        else:
            print("Por favor informe um valor maior do que 0.\n" + linha)

    elif opcao == "1":
        print(tela_saque + "\n" + f"O seu saldo é de: R$ {saldo:}\n" + f"Seu número limite de saques é {SAQUE_LIMITE}." + f"Seu número de saques é {numero_saques}.")
        valor_saque = float(input("Informe o valor à ser sacado: "))

        if valor_saque > saldo:
            print("Você não tem saldo o suficiente para sacar dinheiro.\n Informe um novo valor.\n" + linha)

        elif valor_saque > limite:
            print(f"Seu valor limite de cada saque é R$ {limite}.\nInforme um novo o valor à ser sacado.\n" + linha)

            
        elif numero_saques >= SAQUE_LIMITE:
            print("Você atingiu o limite de saques diários.\n" + linha)

        else:
            valor_saque > 0 and valor_saque <= saldo and saldo > 0 and numero_saques <= SAQUE_LIMITE and valor_saque <= limite
            numero_saques += 1
            saldo -= valor_saque
            print(f"Você sacou R$ {valor_saque}. Aguarde a impressão das notas. Obrigado!\n" + linha)
            extrato += f"Saque: R$ {valor_saque:.2f}\n"

    elif opcao == "2":
        print(tela_extrato)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}\n" + linha)
    
    elif opcao == "3":
        break

    else:
        print("Operação inválida, por favor selecione uma das opções mostradas")
    
