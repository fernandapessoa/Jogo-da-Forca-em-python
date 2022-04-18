#JOGO DA FORCA

import os

os.system('cls')


#VARIÁVEIS DE PROCESSAMENTO
cadaLetra = []
contadorDeErros = 0
contadorDeAcertos = 0
letrasInválidas = []
fim = 1
posição = []
vez = 0
letraOficial = []
listaLinha = []
tentativa = ' '

#VALORES DE ENTRADA DO COMEÇO
print('        JOGO DA FORCA\n\n')
palavra = input('Escolha uma palavra: \n').lower()
gabarito = palavra
palavra = palavra.replace(' ', '-')
palavra = palavra.split()
dica = input('\nDigite a dica da palavra: \n')


#CRIAR A LISTA COM CADA LETRA DA PALAVRA
for n in range (len(palavra)):
    for i in palavra[n]:
        cadaLetra.append(i)

os.system('cls')


#DESENHO DE ACORDO COM CONTADOR DE ERROS
def desenho (contadorDeErros):
    if contadorDeErros == 0:
        os.system('cls')
        print(f'''
                    JOGO DA FORCA

Dica: {dica}
        
__________
|         |
|         
|        
|        
|
|
''')

    elif contadorDeErros == 1:
        os.system('cls')
        print(f'''
                    JOGO DA FORCA

Dica: {dica}
        
__________
|         |
|         O
|         
|        
|
|
''')

    elif contadorDeErros == 2:
        os.system('cls')
        print(f'''
                    JOGO DA FORCA

Dica: {dica}
        
__________
|         |
|         O
|         |
|        
|
|
''')

    elif contadorDeErros == 3:
        os.system('cls')
        print(f'''
                    JOGO DA FORCA

Dica: {dica}
        
__________
|         |
|         O
|        /|
|        
|
|
''')

    elif contadorDeErros == 4:
        os.system('cls')
        print(f'''
                    JOGO DA FORCA

Dica: {dica}
        
__________
|         |
|         O
|        /|\\
|          
|
|
''')

    elif contadorDeErros == 5 :
        os.system('cls')
        print(f'''
                    JOGO DA FORCA

Dica: {dica}
        
__________
|         |
|         O
|        /|\\
|        /
|
|
''')

    elif contadorDeErros == 6:
        os.system('cls')
        print(f'''
                    JOGO DA FORCA

Dica: {dica}
        
__________
|         |
|         O
|        /|\\
|        / \\
|
|

VOCÊ MORREU!!! 
RESPOSTA: {gabarito}
''')
        fim = 0
        y = input()
    

#FUNÇÃO QUE MOSTRA LETRAS E ERROS
def contadorEletras():
    print(f'''
    
Letras inválidas: {letrasInválidas}
Quantidade de erros: {contadorDeErros}''')


#FUNÇÃO QUE MOSTRA OS RISCOS E LETRAS EMBAIXO DA FORCA
def mostraLinhas(tentativa, cadaLetra, contadorDeAcertos, listaLinha):
   
    #cria uma lista com _ e ' ' para cada caractere
    if vez == 0: 
        for n in range (len(cadaLetra)):
            if '-' == cadaLetra[n]:
                listaLinha.append(' ')
                
            else:
                listaLinha.append('_')

    #i é para o indice nao ser string
    i = 0

    #substitui na lista, o elemento pela tentativa se for correspondente
    for n in listaLinha:
        if contadorDeAcertos >= 1:
            if tentativa == cadaLetra[i]:
                listaLinha[i] = str(tentativa)
        i += 1
    
    #w é para o indice nao ser string
    w = 0

    #mostra embaixo da forca as lista com as linhas, letras e espaços
    for n in range (len(listaLinha)):
        print(listaLinha[w], end="")
        w += 1


#INÍCIO DO LAÇO
while fim >= 1:

    desenho(contadorDeErros)
    mostraLinhas(tentativa, cadaLetra, contadorDeAcertos, listaLinha)
    contadorEletras()
    
    vez += 1

    #limite de tentativas porque o boneco da forca tem 6 "partes"
    if contadorDeErros >= 6:
        fim = 0


    #VERIFICAR SE GANHOU
    #caso não tenha _ na listaLinha, acaba (porque completou as letras da forca)
    aindaTem = 0
    for n in listaLinha:
        if (n == "_"):
            aindaTem +=1
    if aindaTem == 0:
        fim = 0
        print (f'''\n\nPARABÉNS!!! VOCÊ ACERTOU\n\n''')

    #if que limita aparecer o resto do programa caso tenha terminado o jogo
    if contadorDeErros < 6 and aindaTem != 0:
            
    #VALOR DE ENTRADA DA TENTATIVA
        tentativa = input('\nFaça sua tentativa: \n')
       
    #CONDICIONAL PARA ESCREVER
        posição.clear()
        for pos,char in enumerate(cadaLetra):
            if (char==tentativa):
                posição.append(pos)
                
        if len(posição) == 0:
            contadorDeErros += 1
            letrasInválidas += tentativa
            print(f'letra {tentativa} não corresponde.')
            y = input()
        else:
            contadorDeAcertos += 1
