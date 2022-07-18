from ast import Try
import random # --> Elementos randomicos
from time import sleep # --> Elementos de espera
r = 1  # --> Resposta de continuação
pj = 0 # --> Pontuação do jogado
pm = 0 # --> Pontuação da máquina (Charlie)
i= 1   # --> Controlador de rodada
ro=10  # --> Controlador base de rodada
jogada=[1,2,3] # --> Objetos de escolha
v = 1  # --> Escolha de objetos

# -------------- Inicio do cabeçalho -------------- #
print('-=-'*20)

print('Bem-vindo ao Jokenpô, eu sou o Charlie :D')

print('-=-'*20)

sleep(2)
jogador = input('Como posso te chamar? ') # --> Nome do jogador
sleep(1)
print('Charlie: Olá {} Conforme formos jogando, sua pontuação aparecerá em \033[1;32mVERDE'.format(jogador))
sleep(1)
# -------------- Fim do cabeçalho -------------- #
print('\033[1;33mCharlie: Vamos começar?')

try:
    r = int(input('[ 1 ] - SIM\n[ 2 ] - Não\n'))
except:
    r = 3
sleep(1)
if r == 1:
    print('\033[1;32mPontuação do jogador {}: {}'.format(jogador,pj))
    print('Pontuação do Charlie: {}'.format(pm))
elif r == 2:
    print('\33[mPoxa, que pena, foi um prazer te conhecer!')
    exit()
else:
    print('Você digitou algo diferente, irei considerar que quer continuar!!')
sleep(1)
print('\033[1;37mIniciando jogo...\033[m\n')
sleep(2)
# -------------- Inicio da rodada -------------- #
while i < ro:
    i = i+1
    e=random.choice(jogada) # --> Escolha da máquina
    print('''\033[mEscolha uma das opções:
    [ 1 ] - Pedra
    [ 2 ] - Papel
    [ 3 ] - Tesoura
    \033[0;31m[ 4 ] - Sair do jogo\033[m''')
    v = int(input())
    sleep(1)

    if v == e:
        print('Charlie: Nós escolhemos a mesma opção. Ninguém ganhou!!'.format(v))
    elif v == 1 and e == 2:
        print('Charlie: Escolhi \033[34mPapel,\033[m e você escolheu \033[34mPedra.\033[1;31m Você perdeu!! haha\033[m')
        pm = pm + 1
    elif v == 1 and e == 3:
        print('Charlie: Eu escolhi \033[34mTesoura, \033[mVocê escolheu \033[34mPedra. \033[1;35mVocê Ganhou! :(\033[m')
        pj = pj + 1
    elif v == 2 and e == 1:
        print('Charlie: Eu escolhi \033[34mPedra, \033[mVocê escolheu \033[34mPapel. \033[1;35mVocê Ganhou! :(\033[m')
        pj = pj + 1
    elif v == 3 and e == 1:
        print('Charlie: Escolhi \033[34mPedra,\033[m e você escolheu \033[34mTesoura.\033[1;31m Você perdeu!! haha\033[m')
        pm = pm + 1
    elif v == 3 and e == 2:
        print('Charlie: Eu escolhi \033[34mPapel, \033[mVocê escolheu \033[34mTesoura. \033[1;35m Você Ganhou! :(\033[m')
        pj = pj + 1

    elif v == 4:
        sleep(1)
        print('\033[1;32m-=-'*3,'Pontuação Final','-=-'*3)
        print('| Pontuação do jogador {}: {}'.format(jogador, pj))
        print('| Pontuação do Charlie: {}'.format(pm))
        print('-=-'*11,)
        sleep(1)
        print('\33[mCharlie: Poxa, que pena, foi um prazer te conhecer!')
        exit()
    sleep(1)
    print('\033[1;32m-=-'*11)
    print('| Pontuação do jogador {}: {}'.format(jogador, pj))
    print('| Pontuação do Charlie: {}'.format(pm))
    print('-=-'*11)
    sleep(1)
    # -------------- Fim da rodada -------------- #
