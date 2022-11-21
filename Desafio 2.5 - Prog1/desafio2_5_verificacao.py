def verificacao_estrela_perceptivel(quant_estrelas, area_telescopio):
    estrelas_perceptiveis = 0
    for estrela in quant_estrelas:
        telescopio_verificacao = area_telescopio * estrela
        if(telescopio_verificacao >= 40000000):
            estrelas_perceptiveis += 1
    print('Quantidade de estrelas que serão percebidas:', estrelas_perceptiveis)

# VERIFICAÇÃO DO PROGRAMA USANDO OS EXEMPLOS DO PDF:

area_telescopio1 = 10000
estrelas_exemplo1 = [4000, 3500, 5100]

area_telescopio2 = 5869
estrelas_exemplo2 = [3975, 14234, 8569]

area_telescopio3 = 2967
estrelas_exemplo3 = [18650, 16338, 2400, 17702, 14619, 13934, 7979, 16316, 10533]

print('Exemplo 1 - ', end='')
verificacao_estrela_perceptivel(estrelas_exemplo1, area_telescopio1)

print('Exemplo 2 - ', end='')
verificacao_estrela_perceptivel(estrelas_exemplo2, area_telescopio2)

print('Exemplo 3 - ', end='')
verificacao_estrela_perceptivel(estrelas_exemplo3, area_telescopio3)