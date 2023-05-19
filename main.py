import random as rd
def jogo_da_forca():
    print('-------- JOGO DA FORCA --------')
    print('----- ADIVINHE O NOME DA COR -----\n')

    Cores= ['AMARELA', 'VERDE', 'ROSA', 'ROXA', 'AZUL', 'BRANCA', 'MARROM', 'VERMELHA', 'PRETA','BRANCA']

    # Função para escolher uma palavra da lista aleatoriamente
    def palavra_aleatoria(Cores):
        tamanho = len(Cores)
        sorteio = rd.randint(1, tamanho)
        palavra_aleatoria = Cores[sorteio]
        return palavra_aleatoria

    # função para localizar as posições de uma letra em uma palavra
    def localizar(texto, palavra):
        posicoes = []
        for i in range(0, len(texto)):
            if texto[i] == palavra:
                posicoes.append(i)
        return posicoes

    palavra = palavra_aleatoria(Cores)
    print(f'DICA: A palavra tem {len(palavra)} letras')

    chances = 0
    pal_secreta = list('_' * len(palavra))
    while chances <= 10:
        letra_digitada = input('Digite somente uma letra: ').upper()
        if letra_digitada in palavra:
            print(f'A letra {letra_digitada} está contida na frase')
            posicao = localizar(palavra, letra_digitada)
            for i in posicao:
                pal_secreta[i] = letra_digitada
            print(pal_secreta)
            opcao = input('Você já sabe qual é o nome da palavra? (S ou N): ')
            if opcao.upper() == 'S':
                resposta = input('Digite o nome da palavra: ')
                if resposta.upper() == palavra:
                    print('------------------------')
                    print(f'Parabéns!!\nA Palavra correta é {palavra}! ')
                    print('------------------------')
                    break
                else:
                    print('Você errou!')
                    print(f'A Palavra correta é {palavra}!')
                    print('-------- X GAME OVER X --------')
                    break
            else:
                print('-----------------------\n')
                print(f'Você ainda tem mais {9 - int(chances)} chances')
        else:
            print(f'A letra {letra_digitada} NÃO está contida na frase')
            print(pal_secreta)
            opcao = input('Você já sabe qual é o nome da palavra? (S ou N): ')
            if opcao.upper() == 'S':
                resposta = input('Digite o nome da palavra: ')
                if resposta.upper() == palavra:
                    print('------------------------')
                    print(f'Parabéns!!\nA Palavra correta é {palavra}!')
                    print('------------------------')
                    break
                else:
                    print('Você errou!')
                    print(f'A Palavra correta é {palavra}!')
                    print('--------GAME OVER--------')
                    break
            else:
                print(f'Você ainda tem mais {9 - int(chances)} chances')
                print('------- ----------------\n')

        chances += 1
        if chances >= 10:
            print('--------GAME OVER--------')
            print(f'A Palavra correta é {palavra}!')
            break


jogo_da_forca()
