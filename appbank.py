import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime 

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

        def __iter__(self):
            return self
        
        def __next__(self):
            try:
                conta = self.contas[self._index]
                return f"""\
                Agência:\t{conta.agencia}
                Número:\t\t{conta.numero}
                Titular:\t{conta.cliente.nome}
                Saldo:\t\tR$ {conta.saldo:.2f}
            """
            except IndexError:
                raise StopIteration
            finally:
                self._index += 1

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def executar_transacao(self, conta, transacao):
        if len(conta.historico.transcoes_dia()) >= 2:
            print("\n@@@ Transação não permitida! Você excedeu o limite diário de transações! @@@")
            return
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)    

class Pessoa_Fisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__ (self, numero, cliente):
        self.saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    @property
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print ("\n@@@ Operação inválida! Você não possui saldo suficiente. @@@")
        elif valor > 0:
            self._saldo -= valor
            print ("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False
        return True

class conta_corrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
    
    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)
    def sacar(self, valor):
        numero_saques = len (
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )
        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques > self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite de sua conta. @@@")
        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número de saques diários excedidos, contate seu banco!. @@@")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
        """









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


def log_transacao(func):
    def envelope(*args,**kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now()}: {func.__name__.upper()}")
        return resultado
    return envelope


@log_transacao
def depositar(clientes)
    




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