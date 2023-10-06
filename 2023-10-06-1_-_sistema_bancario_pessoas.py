# pessoas.py
import contas

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade: int):
        self._idade = idade
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}, {attrs}' #1:

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: contas.Conta or None #3:

if __name__ == '__main__':
    c1 = Cliente(nome = 'Edson', idade = 75)
    c1.conta = contas.ContaCorrente(agencia = 555, conta = 666, saldo = 0, limite = 0)
    print(c1) #2:
    print(c1.conta) #4:
    print()
    c2 = Cliente(nome = 'Rufa', idade = 17)
    c2.conta = contas.ContaPoupanca(agencia = 888, conta = 999, saldo = 0)
    print(c2) #5:
    print(c2.conta) #6:
 

    #1: Este retorno sairá em #2.
    #2: Resposta: Cliente, ('Edson', 75).
    #3: Estudar sintaxe. Ficou boa mesmo?
    #4: Resposta: ContaCorrente, (555, 666, 0, 0).
    #5: Resposta: Cliente, ('Rufa', 17).
    #6: Resposta: ContaPoupanca, (888, 999, 0).