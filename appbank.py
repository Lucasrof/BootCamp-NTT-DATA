menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "1":
        valorDepositado = float(input("Digite o valor a ser depositado : "))

        if valorDepositado > 0:
            saldo += valorDepositado
            print(f'\nDepósito de R$ {valorDepositado:.2f} realizado com sucesso!')
            extrato += (f'\n Depósito: R$ {valorDepositado:.2f}\n')
        else:
            print('A operação falhou! O valor depósitado é inválido.')
            
    elif opcao == "2":
        valorDepositado = float(input("Informe o valor a ser sacado: "))
        
        saldo_insuficiente = valorDepositado > saldo
        valor_excedido = valorDepositado > limite
        quantidade_saques = numero_saques >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("Você não possuí saldo suficiente!")
        elif valor_excedido:
            print("O valor do saque excede o limite da conta!")
        elif quantidade_saques:
            print("A quantidade de saques diários foi excedida! Entr em contato com o seu banco!")
        elif valorDepositado > 0:
            saldo -= valorDepositado
            extrato += (f'\n Saque: R$ {valorDepositado:.2f}\n')
            print(f'\nSaque de R$ {valorDepositado:.2f} realizado com sucesso! Retire as cédulas na boca do caixa')
            numero_saques+=1
        else:
            print("O valor informado para saque é inválido!")    
    
    elif opcao == "3":
        print("\n ********** EXTRATO BANCÁRIO **********")
        print("\n Não foram realizadas movimentações." if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print("\n ********** BANCO  BANCÁRIOS ************")
    
    elif opcao == "0":
        print("Agradecemos a sua preferência!!")
        break
        
    else:
        print("Operação Inválida!, por favor selecione novamente a operação desejada.")