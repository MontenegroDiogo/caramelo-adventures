import winsound
import random
import time

dragao = 120
goblinking = 150
vida = 200
Ragnar = 80
aranha = 150
hp = 150
esqueletoKing = 150

while True:
    
    print("                 Bem vindo ao grande mundo de Whalbior!")
    print('')
    

    print("Antes de iniciarmos sua aventura, me diga, qual dessas classes você deseja começar o jogo?\n")

    print("1.Guerreiro - Você será mais ágil e habilidoso com armas.\nEm breve a classe Mago e Doguinho Caramelo")
    
    
        
    # print("2.Mago - Você vai lutar com magias e será estratégico.\n")
    
    
    
    # print("3.Doguinho Caramelo - Essa raça/classe é apenas para quem deseja resenhar pelo mundo de Whalbior.\n")
    winsound.PlaySound("medieval-inicio.wav", winsound.SND_FILENAME)
    
    

    classe = input("Digite o numero da classe escolhida: ")
    print("")


    if classe.lower() == "1":
            nick = input("Qual será seu nick meu nobre jogador?")
            print("")

            print("Ok {}, conheça a Tink!".format(nick))
            time.sleep(1)
            print("")

            print("Tink: Óla {}, prazer em te conhecer!".format(nick))
            time.sleep(2)
            print("")

            print("1. Olá! O prazer é todo meu!")
            print("2. Oi")
            print("3. ...")

            while True:
                    respostatink = input("Responda a Tink: ")
                    
                    if (respostatink == "1"):
                        print("")
                        print("Você: Olá! O prazer é todo meu!")
                        time.sleep(1)
                        print("Tink: Já gostei de você!")
                        break
                    
                    elif (respostatink == "2"):
                        print("")
                        print("Você: Oi")
                        time.sleep(1)
                        print("Tink: ...")
                        break

                    elif (respostatink == "3"):
                        print("")
                        print("Você: ...")
                        time.sleep(1)
                        print("Tink: nossa...")
                        break
                    
                    else:
                        print("Por gentileza, escolha apenas uma das opções acima.")
                        continue
            print("")
            time.sleep(1)

            print("Tink será a sua fada-guia.\nEla vai te explicar o porque de você estar aqui.")
            time.sleep(1)
            print("")

            print("Tink: Antes, vamos dar uma passadinha no centro de Whalbior.")
            print("")
            time.sleep(1)

                #Msuica ambiental medieval

            print("         VOCÊ CHEGOU AO CENTRO DE WHALBIOR! ")
            print("")
            time.sleep(2)

            print("Tink: Esse aqui é o centro da cidade de Whalbior.")
            print("Tink: Oque achou?")
            print("")
            time.sleep(1)

            print("1. É uma cidade muito linda Tink!")
            print("2. Fede a bosta")
            print("3. ...")
            time.sleep(1)

            
            while True:
                respostatink2 = input("Responda: ")

                if respostatink2 == '1':
                    print("Tink: É realmente uma cidade linda, mas..")
                    time.sleep(1)
                    break
                
                
                elif respostatink2 == '2':
                    print("Tink: Você é bem mau-humorado ein?")
                    time.sleep(1)
                    break
                
                elif respostatink2 == '3':
                    print('Tink: ok...')
                    time.sleep(1)
                    break

                else:
                    print("Escolha apenas uma das opções fornecidas.")
                    continue


            print("Tink: Ultimamente esta sendo muito invadidade por monstros e as vezes o terrivel dragão aparece para nos apavorar!")
            time.sleep(1)

            print("Tink: Inclusive, você foi escolhido para nos salvar desses monstros.")
            time.sleep(1)

            print("Tink: E eu fui escolhida para te guiar, estamos juntos nessa.")
            time.sleep(1)
            print("")

            print("Você: Posso recusar?")
            time.sleep(1)

            print("Tink: Pode sim, mas assim que recusar o governo vai mandar te matar. ")
            time.sleep(2)
            print("")

            print("Tink: Você deseja recusar a missão?")
            time.sleep(1)
            print("")

            print("1.Aceitar")
            print("2.Recusar")

            while True:
                respostatink3 = input("Resposta: ")
                if respostatink3 == '1':
                    print("Tink: Ufa! Eles iriam me matar também caso você tivesse recusado.")
                    break

                elif respostatink3 == "2":
                    #Audio da faca cortando
                    print("Você foi morto pelo governo e Tink acabou sendo morta também por sua culpa.")
                    time.sleep(1)
                    print("Tente novamente!")
                    time.sleep(2)
                    continue

                else:
                    print("Escolha apenas uma das opções fornecidas.")
                    continue

                    



            time.sleep(3)

            print("Tink: Relaxa! Você só foi escolhido porque viram potencial em você. ")
            print("Tink: Deixa eu te mostrar um negócio. ")
            time.sleep(1)

            print("Tink: Os guerrerios que tentaram e voltaram com vida, foram aos poucos fazendo uma mapa da maneira mais fáil de conseguir chegar no temido Dragão Infernal!")
                    
            print("")
            time.sleep(1)

            print("Você: Dragão Infernal?")

            print("")
            time.sleep(1)

            print("Tink: Sim, é porque ele transformou nossa vida em um inferno!")

            print("")
            time.sleep(1)

            print("Você: Entendi, cade o mapa?")
                    
            print("")
            time.sleep(1)

        
            print("Tink: aqui esta!")

            print("")
            time.sleep(1)

            print("Você: Deixa eu ler aqui...")
            #Audio passando folha
            time.sleep(2)
        

            print("Você: Aqui ta dizendo o seguinte:")
            time.sleep(1)
            print("Você: Para realmente derrotar o dragão infernal, vou ter que passar pela Floresta proibida e procurar a Caverna Misteriosa.")
            time.sleep(1)
            print("Você: Após sair da caverna eu Vou me deparar com o Rio de aguas mortas e navegar por ele até achar um Castelo Amaldiçoado.")
            time.sleep(1)
            print("Você: E logo após isso, vou até a montanha aonde geralmente esta o dragão para enfrenta-lo")

            print("")
            time.sleep(1)

            print("Tink: Você tem muito trabalho pela frente, vamos logo!")
            time.sleep(2)

            print("               FLORESTA PROIBIDA  ")
            #AUDIO de floresta ambiente
            time.sleep(2)

            print("Tink: Essa floresta é realmente assustadora {}!".format(nick))
            time.sleep(1)

            print("Tink: Eu soube das muitas historias a respeito dos ataques de goblins que ocorrem muito por aqui")
            time.sleep(1)
            print("")

            print("1. Calma, não vai acontecer nada.")
            print("2. Tomara que eles te sequestrem.")
            print("3. ...")

            while True:
                respostatink4 = input("Responda: ")
                if respostatink4 == "1":
                    print("Você: Calma, não vai acontecer nada.")
                    time.sleep(1)
                    print("Tink: Tomara, obrigado por me acalmar.")
                    break

                elif respostatink4 =='2':
                    print("Você: Tomara que eles te sequestrem.")
                    time.sleep(1)
                    print("Tink: Para! Porque você é assim??")
                    break

                elif respostatink4 =='3':
                    print("Você: ...")
                    time.sleep(1)
                    print("Tink: Você é caladão ein?")
                    break

                else:
                    print("Escolha apenas uma das opções fornecidas.")
                    continue 

            print("Tink: Acho que vamos chegar na carvena mais rapido do que eu pensa--...")
            time.sleep(1)
            print("Tink: GO-GO-GOBLIN GIGANTE!!!!")
            #Audio de monstro 

            print("Você: TINK SE ESCONDA NAS ARVORES AGORA!")
            print("Você: Eu cuido desse grandão")
            #Audio de suspense/ação

            print("Tink: ELE TA INDO PRA CIMA DE VOCÊ {}, CUIDADO!!".format(nick))
            print("")
            time.sleep(1)

            print("Seus ataques disponiveis são:")
            print("1. Ataque leve")
            print("2. Ataque moderado")

            while goblinking > 0:
                ataque = input("Rápido! Qual ataque deseja utilizar?: ")
                if ataque == '1':
                    print("Você esquivou do Goblin King e realizou um ataque leve!")
                    dano = random.randint(10,30)
                    goblinking -= dano
                    print('Você realizou {} de dano no Goblin King, restam {} de vida'.format(dano, goblinking))
                    #audio de espada
                    
                
                elif ataque == '2':
                    print("Você achou abertura e realizou um ataque mais forte!")
                    dano = random.randint(50,70)
                    goblinking -= dano
                    print('Você realizou {} de dano no Goblin King, restam {} de vida'.format(dano, goblinking))
                    #audio de espada
                    

                else:
                    print("Escolha apenas uma das opções fornecidas.")
                    
            
            print("")
            time.sleep(2)
            #audio morrendo
            print("      PARABENS, VOCÊ DERROTOU O PRIMEIRO BOSS!")
            print("")
            #AUDIO de comemoração
            time.sleep(2)

            print("Tink: MATOU??")
            time.sleep(1)
            print("Você: Sim, ele já esta morto.")
            time.sleep(1)
            print("Tink: UFA!")
            time.sleep(1)
            print("Tink: Você é realmente muito bom lutando")
            time.sleep(2)
            print("Tink: VEJA!")
            time.sleep(1)
            print("Tink: A CAVERNA LOGO ALI!")
            time.sleep(1)
            print("Tink: Vamos logo!")
            time.sleep(1)
            print("")
            print("Você: Vamos!")

            print("")
            print("                   Caverna Misteriosa ")
            #audio de caverna

            print("")

            print("Tink: Nossa, como aqui ta escuro!")
            time.sleep(1)
            print("")
            print("Tink: {}, tenta acender alguma tocha para clarear".format(nick))
            time.sleep(1)
            print("")
            print("Você: Perae, deixa eu procurar algo por aqui")
            print("")
            time.sleep(2)
            print("Desconhecido: Toma, usa isso aqui")
            print("")
            time.sleep(2)
            print("Tink: AAAAAAHHHHH!!")
            print("Você: AAAAHHH!!")
            print("")
            time.sleep(1)
            print("Tink: QUEM É VOCÊ??!!")

            print("")
            time.sleep(1)

            print("Desconhecido: Calma, eu não vou fazer nenhum mal a vocês")
            time.sleep(1)
            print("Desconhecido: Não quero entrar em uma luta com o guerreiro ai")
            time.sleep(1)
            print("Tink: Então oq você quer?")
            time.sleep(1)
            print("Desconhecido: Quero apenas me unir a vocês para tentar sair daqui, posso?")
            time.sleep(1)
            print("Tink: Não sei, oq você acha {}?".format(nick))

            print("1. Ajudar")
            print("2. Não Ajudar")

            while True:
                respostatink5 = input("Responda: ")
                if respostatink5 == "2":
                    print("Você: Não acho uma boa ideia, você nem se quer se apresentou.")
                    time.sleep(1)
                    print("Você: Não quero andar com um estranho.")
                    time.sleep(1)
                    print("Ragnar: Me perdoe pela falta de educação, eu me chamo Ragnar.")
                    time.sleep(1)
                    print("Ragnar: Juro que só quero sair daqui, por favor, me ajudem!.")
                    time.sleep(1)
                    print("Tink: Vaai {}, ele só quer sair daqui o coitado.".format(nick))
                    time.sleep(2)
                    print("Você: Não sei...")
                    time.sleep(1)
                    print("Ragnar: Por favor, te imploro, faço oq você mandar")
                    time.sleep(1)
                    print("Você: E é?")
                    time.sleep(1)
                    print("Você: Então fica ai no teu canto que nós vamos seguir sem você! ")
                    time.sleep(1)
                    print("Ragnar: VOCê ESTA ME ZUANDO?! ")
                    time.sleep(1)
                    print("Ragnar: SEU MISERAVEL!! ")
                    time.sleep(1)
                    print("Você: É melhor você se acalmar Ragnar, já estou com minha espada em mãos! ")
                    time.sleep(1)
                    print("Tink: Cuidado {}, ele também tem uma espada".format(nick))
                    time.sleep(1)
                    print("Ragnar: SE EU NÃO VOU SAIR, TAMBÉM NINGUEM VAI!!")
                    #audio de suspense/ação

                    time.sleep(1)
                    print("Tink: CUIDADO, ELE ESTA INDO PRA CIMA DE VOCÊ!")
                    time.sleep(1)
                    print("Você: Esse dai preciso nem me esforçar kkk")
                    print("")
                    time.sleep(2)

                    print("1. Ataque Leve")
                    print("2. Ataque Moderado")

                    while Ragnar > 0:
                        ataque2 = input("Rápido, escolha seu ataque: ")
                        if ataque2 == '1':
                            print("Você realizou um ataque leve e com muito deboche")
                            dano = random.randint(10,30)
                            Ragnar -= dano
                            print('Você realizou {} de dano no pobre do Ragnar, restam {} de vida'.format(dano, Ragnar))
                        
                        elif ataque2 == '2':
                            print("Você realizou um ataque moderado para acabar logo")
                            dano = random.randint(50,70)
                            Ragnar -= dano
                            print('Você realizou {} de dano no pobre do Ragnar, restam {} de vida'.format(dano, Ragnar))

                        else:
                            print("Escolha apenas uma das opções fornecidas.")
                        
                    print("")
                    time.sleep(1)
                    print("                 Você matou o Ragnar") 
                    print("")
                    time.sleep(1)
                    print("Você: Ele praticamente pediu") 
                    print("")
                    time.sleep(1)
                    print("Tink: CREDO!")
                    print("")
                    print("")
                    time.sleep(1)
                    print("Tink: VAMOS SAIR LOGO, EU NÃO AGUENTO MAIS!")
                    print("Você: Vamos!")

                    print("")
                    time.sleep(2)
                    break

                elif respostatink5 == "1":
                    print("Você: Eu até deixo, mas primeiro, qual seu nome?")
                    print("")
                    print("Desconhecido: Ah! Perdão pela minha falta de educação!")
                    time.sleep(1)
                    print("Ragnar: Meu nome é Ragnar, muito prazer em conhece-los!")
                    time.sleep(1)
                    print("")
                    print("Você: Ok, ragnar.")
                    print("Você: Você vai andando na frente e nós atrás.")
                    time.sleep(1)
                    print("")
                    print("Ragnar: Ok.")
                    time.sleep(1)
                    print("")
                    print("Você: Você vai andando na frente e nós atrás.")
                    time.sleep(1)
                    print("")
                    print("Ragnar: Olhem pessoal, acho que já estou vendo a sa--...")
                    time.sleep(2)
                    print("")
                    print("Ragnar: ARANHA GIGANTE!!")
                    print("Tink: ARANHA GIGANTE!!!")
                    print("")
                    #Audio monstro
                    time.sleep(2)
                    print("Você: Corram para atrás das pedras!")
                    time.sleep(1)
                    print("Você: Eu cuido desse monstro!")
                    print("")

                    print("Tink: CUIDADO COM A TEIA!!")
                    print("")
                    time.sleep(1)
                    print("Você: AAHH DROGA!")
                    time.sleep(1)
                    print("Você: ELA ME PRENDEU NAS TEIAS DELA!")
                    print("")
                    time.sleep(1)
                    print("Você: RAGNAR, ME AJUDA!")
                    print("")
                    time.sleep(1)
                    print("Ragnar: Me desculpe, a saida é bem aqui")
                    time.sleep(1)
                    print("Ragnar: Eu tenho que fugir logo!")
                    time.sleep(1)
                    print("")
                    print("             Ragnar foge")
                    time.sleep(1)
                    print("")
                    print("Você: COVARDE!!")
                    print("Tink: COVARDE!!")
                    time.sleep(1)
                    print("")
                    print("Aranha: AAAARRRRGGGHHHH")
                    time.sleep(1)
                    print("")
                    print("         Você corta a teia")
                    time.sleep(1)
                    print("")
                    print("Tink: CUIDADO {}!!".format(nick))
                    time.sleep(2)
                    print("")

                    while aranha > 0:
                        ataque3 = input("Rápido! Qual ataque deseja utilizar?: ")
                        if ataque3 == '1':
                            print("Você esquivou das teias dela e realizou um ataque leve!")
                            dano = random.randint(10,30)
                            aranha -= dano
                            print('Você realizou {} de dano na Aranha, restam {} de vida'.format(dano, aranha))
                            #audio de espada
                    
                
                        elif ataque3 == '2':
                            print("Você esquivou das teias dela e realizou um ataque moderado!")
                            dano = random.randint(50,70)
                            aranha -= dano
                            print('Você realizou {} de dano no aranha, restam {} de vida'.format(dano, aranha))
                            #audio de espada
                
                
                            print("")
                            print("             Você Derrotou a aranha")
                            print("")
                            time.sleep(1)
                            print("Tink: VAMOS SAIR LOGO, EU NÃO AGUENTO MAIS!")
                            print("Você: Vamos!")
                            print("")
                            time.sleep(2)

                        else:
                            print("Escolha apenas uma das opções fornecidas.")

            print("             Rio das Aguas mortas ")

            print("")
            time.sleep(1)

            print("Você: Vamos Tink, entra logo nesse barco abandonado, precisamos atravessar o rio")

            print("")
            time.sleep(1)

            print("Tink: Vou mesmo, aqui ta tão estranho")

            print("Voce: Temos que ter muita atencao por aqui")
            time.sleep(1)
            print("Voce: Esta tudo muito calmo")
            time.sleep(2)
            print("Estranhamente calmo...")
            #barulhp de suspense
            
            print("")
            #barulho de peixe mergulhando
            print("Tink: AAAAIII")
            time.sleep(2)
            print("Tink: QUE SUSTO!")
            time.sleep(1)
            print("voce: kkkkkk calma Tink, é só--...")
            time.sleep(3)
            print("voce: ...--um peixinho")
            time.sleep(2)
            print("Tink: HOMEM PEIXEEEE!!!")
            #AUDIO grito monstro
            time.sleep(1)
            print("Voce: A cacete!")
            time.sleep(1)
            print("Voce: Esses monstros não dão uma tregua!")
            print("")
            time.sleep(2)
            print("Homem-Peixe: Calma fadinha, eu não vim te fazer mal")
            time.sleep(2)
            print("Homem-Peixe: Fiquei apenas, curioso, pois nunca vi voces navegando nas minhas aguas ")
            time.sleep(2)
            print("")
            print("Voce: Fala meu peixo, tudo bem?")
            print("")
            time.sleep(2)
            print("Homem-peixe: O que estao fazendo nas minhas aguas?!")
            
            print("")
            time.sleep(2)
            print("1. Apenas querendo chegar ao nosso destino")
            print("2. Não interessa")
            print("3. Diminui o tom de voz ou você vai virar sardinha ")

            while True:
                resphp = input("Responda: ")
                if resphp == '1':
                    print("Você: Apenas querendo chegar ao nosso destino")
                    print("")
                    time.sleep(2)
                    print("Homem-peixe: Não ligo! Saiam daqui por bem ou por mal!")
                    print("Você: *puxa a espada*\nVou passar e acabou!")
                    break
            
                elif resphp == '2':
                    print("Você: Não interessa")
                    time.sleep(2)
                    print("Homem-peixe: Vou te ensinar a ter educação!")
                    time.sleep(1)
                    print("Você: vem pra cima!")
                    break

                elif resphp == '3':
                    print("Você: Diminui o tom de voz ou você vai virar sardinha")
                    time.sleep(1)
                    print("Homem-peixe: AAHH SEEU!")
                    break

                else:
                    print("Escolha apenas uma das opções acima.")
                    continue


            while hp > 0 and vida > 0:
                print("Escolha seu ataque:")
                print("1. Ataque Leve")
                print("2. Ataque Moderado")
                ataque_jogador = input("Digite o número do seu ataque: ")
                if ataque_jogador == "1":
                    dano_jogador = random.randint(20, 40)
                    print("Você atacou o Homem-Peixe com um ataque leve, causando {} de dano!".format(dano_jogador))
                elif ataque_jogador == "2":
                    dano_jogador = random.randint(40, 60)
                    print("Você atacou o Homem-Peixe com um ataque moderado, causando {} de dano!".format(dano_jogador))
                else:
                    print("Por favor, escolha um ataque válido.")

                hp -= dano_jogador
                if hp <= 0:
                    print("Você derrotou o Homem-Peixe!")
                    break

                print("Homem-Peixe contra-ataca!")
                danohp = random.randint(20, 30)
                print("Homem-Peixe ataca você, causando {} de dano!".format(danohp))
                vida -= danohp
                if vida <= 0:
                    print("Você foi derrotado pelo Homem-Peixe!")
                    break

            time.sleep(2)
            print("Tink: UFA! esses monstros não param")
            time.sleep(2)
            print("Você: Verdade!")
            time.sleep(2)
            print("Você: Vamos, chegamos no castelo!")
            time.sleep(2)
            print("")

            print("             CASTELO AMALDIÇOADO ")

            time.sleep(2)
            print("")

            print("Tink: Olá, tem alguem AI-AI-ai-ai")
            time.sleep(1)
            print("Tink: escuta o eco absurdo desse lgar sinistro")
            time.sleep(1)
            print("Você: Cuidado Tink, aqui pode ter muitas armadihas")
            time.sleep(2)
            print("Você: Tink??")
            time.sleep(2)
            print("Tink: AAAAAHHHHH!!")
            time.sleep(1)
            print("Tink: SOCORRO {}, ACABEI DE CAIR NESSE BURACO!!".format(nick))
            time.sleep(1)
            print("Você: Se machucou?")
            time.sleep(1)
            print("Tink: Não muito")
            time.sleep(1)
            print("Você: Então voa até aqui pq você é uma fada")
            print("")
            time.sleep(2)
            print("EsqueletoKing: QUEM OUSA PERTUBAR MEU SOSSEGO??")
            time.sleep(2)
            print("EsqueletoKing: QUEREM A ESPADA TAMBÉM?\nVOCÊS VÃO MORRER TENTANDO COMO OS OUTROS!!")
            print("")
            time.sleep(2)
            print("Tink: CUIDADO {}, O ESQUELETÃO VAI TE PEGAR!".format(nick))
            print("")
            time.sleep(2)
            print("{} desvia do esqueleto".format(nick))
            print("")
            time.sleep(1)
            print("EsqueletoKing: VOU TE MATAR!!")

            while esqueletoKing > 0 and vida > 0:
                print("Escolha seu ataque:")
                print("1. Ataque Leve")
                print("2. Ataque Moderado")
                ataque_jogador1 = input("Digite o número do seu ataque: ")

                if ataque_jogador1 == "1":
                    dano_jogador1 = random.randint(20, 40)
                    print("Você atacou o esqueletão com um ataque leve, causando {} de dano!".format(dano_jogador1))
                elif ataque_jogador1 == "2":
                    dano_jogador1 = random.randint(40, 60)
                    print("Você atacou o esqueletão com um ataque moderado, causando {} de dano!".format(dano_jogador1))
                else:
                    print("Por favor, escolha um ataque válido.")
                    continue

                esqueletoKing -= dano_jogador1

                if esqueletoKing <= 0:
                    print("Você aproveita que ele esta caido e consegue pegar a espada lendaria")
                    time.sleep(2)
                    print("Com a espada você finaliza e mata o Esqueleto")
                    
                    break

                print("esqueletoKing contra-ataca!")
                danoe = random.randint(10, 20)
                print("esqueletoKing ataca você, causando {} de dano!".format(danoe))
                vida -= danoe
                if vida <= 0:
                    print("Você foi derrotado pelo esqueletoKing!")
                    break

    print("")
    time.sleep(2)
    print("Esqueletão: AAAHHH MALDITOO!!")
    #AUDIO DE RAIO
    print("CAIU UM RAIO APÓS A MORTE DO ESQULETO!")
    print("")
    time.sleep(2)
    print("Tink: O DRAGÃO INFERNAL TA AQUI!!!")
    print("")
    time.sleep(2)
    print("Você: Merda! O raio que caiu após a morte do esqueleto acabou chamando a atenção dele")
    print("")
    time.sleep(2)
    print("Você: É AGORA TINK! ")
    time.sleep(2)
    print("Você: É VENCER! ")
    time.sleep(2)
    print("Você: OU MORRER! ")
    print("")
    time.sleep(2)

    print("               FASE FINAL")
    print("            O DRAGÃO INFERNAL")
    #AUDIO grito de dragão

    print("")
    time.sleep(2)
    print("Tink: SE PREPARA!")
    time.sleep(2)

    while dragao > 0 and vida > 0:
                print("Essa é sua ultima luta, escolha bem os ataques:")
                print("1. Ataque Leve")
                print("2. Ataque Moderado")
                ataque_jogador2 = input("Digite o número do seu ataque: ")

                if ataque_jogador2 == "1":
                    dano_jogador2 = random.randint(20, 40)
                    print("Você atacou o Dragão com um ataque leve, causando {} de dano!".format(dano_jogador2))
                elif ataque_jogador2 == "2":
                    dano_jogador2 = random.randint(40, 60)
                    print("Você atacou o Dragão com um ataque moderado, causando {} de dano!".format(dano_jogador2))
                else:
                    print("Por favor, escolha um ataque válido.")
                    continue

                dragao -= dano_jogador2

                if dragao <= 0:
                    print("VOCÊ FINALMENTE DERROTOU O TERRIVEL DRAGÃO INFERNA")
                    time.sleep(2)
                    print("VOCÊ É O ORGULHO DO REINO!")
                    
                    break

                print("Dragão contra-ataca!")
                danog = random.randint(10, 20)
                print("Dragão ataca você, causando {} de dano!".format(danog))
                vida -= danog
                if vida <= 0:
                    print("Você foi derrotado pelo Dragão!")
                    break

            #audio we are the champions





  
    




                

                    










                                            














                        




                


                




        
             
                    

    #         missao1 = input("Óla, me chamo Rub.\*-nPoderia me ajudar com uma missão?(sim/não)")
    #         if missao1 == "sim":
    #             print("Ótimo, vá ate a floresta densa e procure pela minha filha que sumiu a 2 dias. te garanto uma ótima recompensa!")
    #             meio = input("Você deseja ir de barco ou cavalo?")
    #             if meio == "barco":
    #                 print("Você escolheu ir de barco e chegou em 2 dias.")
    #                 print("Você se deparou com um pedaço de um vestido, deve ser da filha do homem.")
    #                 winsound.PlaySound("girl-scream.wav", winsound.SND_FILENAME)
    #                 print("Veja, ela esta sendo levada por um grupo de goblins")
    #                 while True:
    #                     ato = input("Você prefere lutar com eles ou segui-los desfarçadamente?(lutar/seguir)")
    #                     if ato == "lutar":
    #                         print("Você morreu por tentar lutar com todos, escolha certo agora")
    #                     else:
    #                         print("Você continua sua caminhada ao longo da estrada, com a consciência pesada de ter agido de maneira indiferente quanto a situação. \n" "Seu lixo de ser-humano")
    #                         print("Você se depara com uma pequena cidade no horizonte de sua jornada!")
    #                         winsound.PlaySound("brilho.wav", winsound.SND_FILENAME)
    #                         time.sleep(1)
    #                         print("Bem vindo a Ghanor, aventureiro!")
    #                         print("Ao passar pelos grandes portões em formato de arco da cidade, você se depara com uma região balceda, uma síntese de São Paulo com Amazonas, inclusive com os vendedores da 25 de março populando as vielas da cidade.")
    #                         print(f"O que desejas fazer {nick}?")

    #                         while True:
    #                             quest = input("1. Seguir para a Taverna = \n"
    #                                         "2. Dialogar com um dos vendedores da 25 de março = \n"
    #                                         "3. Seguir para o centro da cidade = \n"
    #                                         "4. Seguir para o Dragon's Lair = \n")
    #                             if quest == "1":
    #                                 print("Você seguiu caminhando para a Taverna, à procura de sabe-se lá o que")
    #                                 break
                                
    #                        
    #                             elif quest == "4":
    #                                 print("Você segue o seu caminho para o Dragon's Lair")
    #                                 print("O cheiro de enxofre e fumaça se difunde pelo ar... A sensação de que algo errado não está certo, perpetua-se pela sua cabeça... Quando derrepente")
    #                                 print("UM DRAGÃO SURGE EM SUA FRENTE!")
    #                                 print("Para seu azar, meu amigo você só tem uma opção... A outra não era tão boa para você. LUTAR!")
    #                                 print("Você se prepara para dar um ataque: Você tem três opções: \n 1. Ataque leve \n 2. Ataque Médio e \n 3. Ataque pesado \n O que deseja fazer?:")
    #                                 while dragao > 0:
    #                                     ataque = input("Digite aqui o seu ataque: ")
    #                                     if ataque == "1":
    #                                         print("Você realizou um ataque leve")
    #                                         dano = random.randint(10,30)
    #                                         dragao = max(0, dragao - dano)
    #                                         print(f'Você realizou {dano} de Dano no Dragão, restam {dragao} de vida')
    #                                     elif ataque == "2":   
    #                                         print("Você realizou um ataque médio")
    #                                         dano = random.randint(50,70)
    #                                         dragao = max(0, dragao - dano)
    #                                         print(f'Você realizou {dano} de Dano no Dragão, restam {dragao} de vida')
    #                                     elif ataque == "3":
    #                                         print("Você realizou um ataque pesado")
    #                                         dano = random.randint(70,95)
    #                                         dragao = max(0, dragao - dano)
    #                                         print(f'Você realizou {dano} de Dano no Dragão, restam {dragao} de vida')
    #                                 print("Você derrotou o drãgão, Parabéns :)")
    #                                 break
    #                         break
    # #     elif():
    #         sexoh.lower() == "mulher"
    #         nick = input("Qual seu nome, minha cara?")
    #         print("Ok {}, vamos começar a aventura!".format(nick))
    #         print("Você esta no centro da cidade e ja tem uma missão a sua espera")
    #         missao1 = input("Óla, me chamo Rub.\nPoderia me ajudar com uma missão?(sim/não)")
    #         if missao1 == "sim":
    #             print("Ótimo, vá ate a floresta densa e procure pela minha filha que sumiu a 2 dias. te garanto uma ótima recompensa!")
    #             meio = input("Você deseja ir de barco ou cavalo?")
    #             if meio == "barco":
    #                 print("Você escolheu ir de barco e chegou em 2 dias.")
    #                 print("Você se deparou com um pedaço de um vestido, deve ser da filha do homem.")
    #                 winsound.PlaySound("girl-scream.wav", winsound.SND_FILENAME)
    #                 print("Veja, ela esta sendo levada por um grupo de goblins")
    #                 while True:
    #                     ato = input("Você prefere lutar com eles ou segui-los desfarçadamente?(lutar/seguir)")
    #                     if ato == "lutar":
    #                         print("Você morreu por tentar lutar com todos, escolha certo agora")
    #                     else:
    #                         print("Você continua sua caminhada ao longo da estrada, com a consciência pesada de ter agido de maneira indiferente quanto a situação. \n" "Seu lixo de ser-humano")
    #                         print("Você se depara com uma pequena cidade no horizonte de sua jornada!")
    #                         winsound.PlaySound("brilho.wav", winsound.SND_FILENAME)
    #                         time.sleep(1)
    #                         print("Bem vindo a Ghanor, aventureiro!")
    #                         print("Ao passar pelos grandes portões em formato de arco da cidade, você se depara com uma região balceda, uma síntese de São Paulo com Amazonas, inclusive com os vendedores da 25 de março populando as vielas da cidade.")
    #                         print(f"O que desejas fazer {nick}?")

    #                         while True:
    #                             quest = input("1. Seguir para a Taverna = \n"
    #                                         "2. Dialogar com um dos vendedores da 25 de março = \n"
    #                                         "3. Seguir para o centro da cidade = \n")
    #                             if quest == "1":
    #                                 print("Você seguiu caminhando para a Taverna, à procura de sabe-se lá o que")
    #                                 break
    #                             elif quest == "2":
    #                                 print("Você segue em direção a um dos distintos mercantes que se encontram nessa rua.")
    #                                 time.sleep(1)
    #                                 winsound.PlaySound("resident-evil-4-merchant.wav", winsound.SND_FILENAME)
    #                                 print("O que deseja adquirir?")

    #                                 marketplace = [
    #                                     {'iD': 1, 'Item': '.38 enferrujado', 'Preço': 25,},
    #                                     {'iD': 2, 'Item': 'Espada bastarda', 'Preço': 150},
    #                                     {'iD': 3, 'Item': 'Arco capenga', 'Preço': 100},
    #                                     {'iD': 4, 'Item': 'Alaúde Encantado', 'Preço': 300},
    #                                     {'iD': 5, 'Item': 'Curso de DayTrade da Binomo', 'Preço': 250},
    #                                 ]
    #                                 print(f"Aqui está a lista de itens que você pode comprar: {marketplace}")
    #                                 while True:
    #                                     item = input("Digite o ID do item que você quer comprar: ")
    #                                     if item.isdigit():
    #                                         item = int(item)
    #                                         if 0 < item <= len(marketplace):
    #                                             item_selected = marketplace[item - 1]
    #                                             if cartao >= item_selected['Preço']:
    #                                                 print(f"Você comprou o {item_selected['Item']}")
    #                                                 inventario.append(item_selected['Item'])
    #                                                 cartao -= item_selected['Preço']
    #                                                 print(f"Você tem {cartao} em seu cartão")
    #                                                 time.sleep(1)
    #                                                 winsound.PlaySound("coin.wav", winsound.SND_FILENAME)
    #                                                 while True:
    #                                                     continuar = input("Você quer continuar comprando? (sim/não): ")
    #                                                     if continuar.lower() == "sim":
    #                                                         break
    #                                                     elif continuar.lower() == "não":
    #                                                         break
    #                                                     else:
    #                                                         print("Por favor, responda 'sim' ou 'não'.")
    #                                                         continue
    #                                                 if continuar.lower() == "não":
    #                                                     break
    #                                             else:
    #                                                 print("Você não tem dinheiro suficiente para comprar esse item.")
    #                                         else:
    #                                             print("ID inválido. Por favor, digite um ID válido.")
    #                                     else:
    #                                         print("Entrada inválida. Por favor, digite um ID numérico.")
    #                                 break
    #                             elif quest == "3":
    #                                 print("Você segue o seu caminho para o centro da cidade")
    #                                 print("Esta é uma versão DEMO do jogo: PyGame - Um projeto de Diogo, para acessar a versão final, por favor adquira o produto no link a seguir: https://github.com/MontenegroDiogo/projeto-jogo-else/blob/main/index.py")
    #                                 break
    #                         break
        
    #     else:
    #         print("Por gentileza, escolha se quer ser Homem ou Mulher.")

    # elif classe.lower() == "hp":
    #     nick = input("Qual seu nome, meu peixo?")
    #     print("Ok {}, vamos começar a aventura!".format(nick))
    #     print("Pera...")
    #     print("Sheeeeee")
    #     print("Infelizmente, meu amigo você spawnou em Hellcife, água aqui é algo situacional, vamos ver se você dá sorte de cair em um dia bom")
    #     dia = random.randint(0,10)
    #     if dia >= 0 and dia < 10:
    #         print("Peixe fora dágua não rola, rapaz")
    #         break
    #     else:
    #         print("K, boa tentativa")
    #         break
        
    # elif classe.lower() == "caramelo":
    #     print("Ótimo, você será o Doguinho Caramelo!\nVamos começar!")
    #     destino1 = input("Você chegou na praça e encantou a todos, um homem desconhecido aparece querendo te levar para a casa dele.\nVocê vai ou corre?(Vou/vou nada)")
    #     if(destino1.lower() == "vou"):
    #         print("Por ser um Doguinho Caramelo você foi de boinha com o homem.\nChegando lá você é muito bem recebido pela familia dele e já almoça junto")
    #         break
    #     else:
    #         print("Você se saiu e correu para a floresta")
    #         print("Chegando lá você se depara com um grupo de jovens degustando cogumelos\nEles começam a fazer carinho e você, como um cachorro faz, cheira e come um dos cogumelos.")
    #         print("Logo após isso todos ficam preocupados com você pois não sabem a reação que pode causar em um cachorro, mas, em questão de segundos começam a surgir alguns goblins violentos e todos começam a correr.")
    #         ato1 = input("Você começa a fugir também mas percebe que uma das jovens esta sendo raptada, você deixa pra lá ou vai salva-la?(salvar/fugir)")
    #         if(ato1.lower() == "salvar"):
    #             print("Você decidiu salvar a menina mas acaba cercado por dois goblins.\nMas assim que percebem que você é um doguinho caramelo eles te fazem muito carinho e vão embora") 

