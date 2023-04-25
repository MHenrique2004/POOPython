from pessoa import Pessoa as ps


pessoa1 = ps('joao', 'das neve', 22, 'winterfel')
pessoa2 = ps('beatriz', 'bea', 19, 'recife', False, False)

pessoa1.apresentar()
pessoa2.apresentar()

pessoa2.comer('maca')

pessoa2.acordar()
pessoa2.comer('banana')

pessoa2.comer('macarrao')

print(pessoa1.nacionalidade)
print(pessoa2.nacionalidade)

pessoa2.nacionalidade = 'chines'

print(pessoa2.nacionalidade)

print(pessoa1.__dict__)
print(ps.__dict__)