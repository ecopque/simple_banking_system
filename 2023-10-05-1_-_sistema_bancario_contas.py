# contas.py
import abc

class Conta(abc.ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0) -> None: #1: #5:
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    @abc.abstractmethod
    def sacar(self, valor: float) -> float: ... #2:
    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes (f'Depósito: {valor}')
        return self.saldo #3:
    def detalhes(self, msg: str ='') -> None: #4:
        print(f'O seu saldo é {self.saldo:.2f}. {msg}')
        print('--')
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}, {attrs}'
#
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'Saque: {valor}')
            return self.saldo
        else:                 
            print('Não foi possível sacar o valor desejado!')
            self.detalhes(f'Valor de saque negado: {valor}')
            return self.saldo
#
class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'Saque: {valor}')
            return self.saldo
        else:
            print('Não foi possível sacar o valor desejado!')
            print(f'Seu limite é: {-self.limite:.2f}')
            self.detalhes(f'Valor de saque negado: {valor}')
            return self.saldo
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}, {attrs}'
#
if __name__ == '__main__':
    cp1 = ContaPoupanca(agencia = 111, conta = 222, saldo = 100)
    cp1.sacar(1) #6:
    cp1.depositar(2) #7:
    cp1.sacar(1) #8:
    print('#####')
    cc1 = ContaCorrente(agencia = 333, conta = 444, saldo = 50, limite=100)
    cc1.sacar(1) #9:
    cc1.depositar(2) #10:
    cc1.sacar(100) #11:
    cc1.sacar(55) #12:

#1: This "agencia: int" is typing, meaning I want my account to be int.
#2: "-> float", that it be float and return float to me.
#3: Put the mouse over it and see the indication that it's already float. Beautiful! ;-)
#4: It didn't need to be typed, because it's already ready. But okay, string. And as for None, it's because the method doesn't return anything, so None.
#5: As the method doesn't return anything, then None.
#6: Response: Your balance is 99.00. Withdrawal: 1.
#7: Response: Your balance is 101.00. Deposit: 2.
#8: Response: Your balance is 100.00. Withdrawal: 1.
#9: Response: Your balance is 49.00. Withdrawal: 1.
#10: Response: Your balance is 51.00. Deposit: 2.
#11: Response: It was not possible to withdraw the desired amount! | Your limit is: -100.00 | Your balance is -49.00. Denied withdrawal amount: 55.

##########

# Aqui temos um exercício com "abstração", "herança", "encapsulamento" e "polimorfismo".
# Proposta: criar um sistema bancário que possui clientes, contas e um banco. A idéia é que o cliente tenha uma conta (poupança e corrente) e que possa sacar/depositar nesta mesma conta. Contas corrente tem um limite/crédito extra.
'''Dicas:
. Criar classe CLIENTE que herda da calsse PESSOA (herança):
    . PESSOA tem NOME e IDADE (com getters);
    . CLIENTE tem conta (agregação da classe CONTACORRENTE ou CONTAPOUPANÇA);

. Criar classes CONTAPOUPANÇA e CONTACORRENTE que herdam de CONTA:
    . CONTACORRENTE deve ter um limite/crédito extra;
    . CONTAS devem ter AGÊNCIA, NÚMERO DA CONTA e SALDO;
    . CONTAS devem ter método para depósito;
    . CONTA (super classe) deve ter um método sacar abstrato (abstração e polimorfismo, ou seja, as subclasses que implementam o método sacar).

. Criar classe BANCO para agregar classes de clientes e de contas (agregação);

. BANCO será responsável por autenticar o cliente e as contas da seguinte maneira:
    . BANCO tem CONTAS e CLIENTES (agregação);
    . Checar se a AGÊNCIA é daquele BANCO;
    . CHECAR se o CLIENTE é daquele BANCO;
    . CHECAR se a CONTA é daquele BANCO;

. Só será possível SACAR se passar na autenticação do BANCO (descrito acima);

. Banco autentica  por um método (autenticar).
'''
