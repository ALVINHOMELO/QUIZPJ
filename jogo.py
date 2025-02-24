#exibe uma mensagem de boas vindas na tela
print("Seja Bem-Vindo ao jogo do Alvinho.")

#variavel para contar os pontos
pontos = 0

#aparece a pergunta
#a pessoa responde
#pergunta 1
pergunta = input("Como eles se transformam? \na)Batendo no relógio\nb)Encostando no cristal PJ\nc)Tentando fazer uma das suas habilidades\n")

#verifica a resposta

#se a pessoa responder certo, ela vai ganhar um ponto
if (pergunta == "a"):
    pontos = pontos + 1
    print("você acertou! seus pontos: ", pontos)
#se a pessoa errar a resposta
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)


#pergunta 2
pergunta = input("De onde vem o poder deles?\na)Cristal PJ\nb)PJ Animais\nc)Do relógio deles\n")

if (pergunta == "a"):
    pontos = pontos + 1
    print("Você acertou! seus pontos: ", pontos)
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)


#pergunta 3
pergunta = input("Amaya se transforma en qual animal?\na)Coruja\nb)Gato\nc)Largato\n")

if (pergunta == "a"):
    pontos = pontos + 1
    print("Você acertou! Seus pontos: ", pontos)
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)


#pergunta 4
pergunta = input("Qual o nome verdadeiro do menino gato?\na)Romeu\nb)Conor\nc)Greg\n")

if (pergunta == "b"):
    pontos = pontos + 1
    print("Você acertou! Seus pontos: ", pontos)
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)


#pergunta 5
pergunta = input("Qual é o país da Anyu?\na)Polônia\nb)Inglaterra\nc)China\n")

if (pergunta == "c"):
    pontos = pontos + 1
    print("Você acertou! Seus pontos: ", pontos)
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)

#pergunta 6
pergunta = input("Qual é o veículo do Romeu?\na)Cavalo de Tróia\nb)Máquina Voadora\nc)Impressora 3D\n")

if (pergunta == "b"):
    pontos = pontos + 1
    print("Você acertou! Seus pontos: ", pontos)
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)

#pergunta 7
pergunta = input("Quantos anos a Corujita tem?\na)5 anos\b)7 anos\nc)6 anos\n")

if (pergunta == "c"):
    pontos = pontos + 1
    print("Você acertou! Seus pontos: ", pontos)
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)

#pergunta 8
pergunta = input("Quais são os podere do menino gato?\na)Listras, laser de gelo, velocidade, pulo do gato, escalar e brilhar\nb)rapidez, força, invisibilidade, grudar na parede e voar\nc)Listras de gato, velocidade, pulo e escalar\n")

if(pergunta == "c"):
    pontos = pontos + 1
    print("Você acertou! Seus pontos: ", pontos)
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)


#pergunta 9
pergunta = input("Quantos poderes a corujita tem?\na)6\nb)5\nc)10\n")

if (pergunta == "b"):
    pontos = pontos + 1
    print("Você acertou! Seus pontos: ", pontos )
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)


#pergunta 10
pergunta = input("Quais são os poderes do lagartixo?\na)Escudo de lagarto, invisibilidade, superforça, mudar de cor e brilhar.\nb)Voar, soltar listras e nadar. \nc)Soltar teias e ficar invisivel. ")

if(pergunta == "a"):
    pontos = pontos + 1
    print("Você acertou! Seus pontos: ", pontos)
else:
    pontos = pontos - 1
    print("Você errou! Seus pontos: ", pontos)






