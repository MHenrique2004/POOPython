class Pessoa:
    
    nacionalidade = 'brasileiro'
    
    def __init__(self, nome, apelido, idade, rua, alimentado = True, acordado = True):
        self.nome = nome
        self.apelido = apelido
        self.idade = idade
        self.rua = rua
        self.alimentado = alimentado
        self.acordado = acordado
        
    def apresentar(self):
        if self.acordado:
            print('Ola, meu nome e:', self.nome)
        else:
            print('ZZZZZ')
        
    def falar(self):
        print('Oi, tudo bem?')
        
    def acordar(self):
        self.acordado = True
        self.alimentado = False
        print(self.nome, 'acordado')
        
    def cumprimentar(self):
        if self.acordado:
            print('Ola, tudo bem')
        else:
            print('ZZZZ')
            
    def dormir(self):
        print('ZZZZ')
        self.acordado = False
        
    def comer(self, alimento):
        if self.acordado and not self.alimentado:
            self.alimentado = True
            print('comendo', alimento)
        elif self.acordado and self.alimentado:
            print('não estou com fome')
        else:
            print('ZZZZ')