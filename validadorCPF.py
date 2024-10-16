# Validador de CPF

cpf = input('Digite seu CPF: ').replace('-', '').replace('.','') # Recebe o CPF do usúario
# O replace é para deixar somente os números
nove_digitos = cpf[:9] # Pega os nove primeiros digitos do cpf
dez_digitos = cpf[:10] # Pega os dez primeiros digitos do cpf
contador1 = 10 # Contador necessário para a validação do primeiro digito
contador2 = 11 # Contador necessário para a validação do segundo digito
resultado1 = 0 # Variavel para o calculo de validação do cpf
resultado2 = 0 # Variavel para o calculo de validação do cpf

for digito in nove_digitos:
    """
    Começamos utilizando os 9 primeiros dígitos multiplicando-os pela
    sequência decrescente de 10 à 2 e somamos esse resultado.

    exemplo:
    1	4	5	3	8	2	2	0	6
    X	X	X	X	X	X	X	X	X
    10	9	8	7	6	5	4	3	2
    10	36	40	21	48	10	8	0	12

    """
    resultado1 += (int(digito) * contador1)
    contador1 -= 1

"""
É feito o calcúlo da soma da multiplicação de cada número (resultado1) vezes 10 e
depois pega o resto da divisão dessa multiplicação por 11
"""
primeiro_digito = (resultado1 * 10) % 11

if primeiro_digito > 9:
    print('O primeiro digito do CPF é 0')
    # Caso seja maior que 9, o primeiro digito é 0
else:
    print(f'O primeiro digito do CPF é {primeiro_digito}')
    # Caso seja menor ou igual a 9, o primeiro digito é o próprio número

for digito2 in dez_digitos:
    """
    Começamos utilizando os 10 primeiros dígitos multiplicando-os pela
    sequência decrescente de 11 à 2 e somamos esse resultado.

    exemplo:
    1	4	5	3	8	2	2	0	6   2
    X	X	X	X	X	X	X	X	X   X
    11  10	9	8	7	6	5	4	3	2
    11	40	45	24	56	12	10	0	18  4

    """
    resultado2 += (int(digito2) * contador2)
    contador2 -= 1

"""
É feito o calcúlo da soma da multiplicação de cada número (resultado2) vezes 10 e
depois pega o resto da divisão dessa multiplicação por 11
"""
segundo_digito = (resultado2 * 10) % 11

if segundo_digito > 9:
    print('O segundo digito do CPF é 0')
    # Caso seja maior que 9, o segundo digito é 0
else:
    print(f'O segundo digito do CPF é {segundo_digito}')
    # Caso seja menor ou igual a 9, o segundo digito é o próprio número

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if cpf_gerado == cpf: # Se o cpf gerado com as validações for igual ao cpf digitado, ele é valido
    print(f'O CPF {cpf} é valido!')
else:
    print(f'O CPF {cpf} é invalido!')