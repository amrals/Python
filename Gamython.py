from random import randint

vontade = 1

print("#####     Seja bem vindo ao Gamython      #####")

while vontade == 1:
    print("1 - Criar personagem")
    print("0 - Sair")

    escolha = input()

    if(escolha == '1'):

        print("Digite o nome do seu personagem \n")
        nomePersonagem = str(input())

        print("Escolha o sexo do seu personagem")
        print("1 - Masculino")
        print("2 - Feminino")
        sexoPersonagem = int(input())

        if sexoPersonagem == 1:
            print("Escolha a classe do seu personagem")
            print("1 - Guerreiro")
            print("2 - Mago")
            print("3 - Ladino")
            classePersonagem = int(input())

        elif sexoPersonagem == 2:
            print("Escolha a classe do seu personagem")
            print("1 - Guerreira")
            print("2 - Maga")
            print("3 - Ladina")
            classePersonagem = int(input())

        if classePersonagem == 1:

            class Guerreiro:
                def __init__(self, nomePersonagem, sexoPersonagem):
                    self.nome = nomePersonagem
                    if sexoPersonagem == 1:
                        self.classe = "Guerreiro"
                    elif sexoPersonagem == 2:
                        self.classe = "Guerreira"
                    self.forca = 100
                    self.magia = 10
                    self.inteligencia = 50

                def exibir(self):
                    print("Nome: ", self.nome)
                    print("Classe: ", self.classe)
                    print("Força: ", self.forca)
                    print("Magia: ", self.magia)
                    print("Inteligencia: ", self.inteligencia)
            
            personagem = Guerreiro(nomePersonagem, sexoPersonagem)
        
        elif classePersonagem == 2:

            class Mago:
                def __init__(self, nomePersonagem, sexoPersonagem):
                    self.nome = nomePersonagem
                    if sexoPersonagem == 1:
                        self.classe = "Mago"
                    elif sexoPersonagem == 2:
                        self.classe = "Maga"
                    self.forca = 10
                    self.magia = 100
                    self.inteligencia= 70
                
                def exibir(self):
                    print("Nome: ", self.nome)
                    print("Classe: ", self.classe)
                    print("Força: ", self.forca)
                    print("Magia: ", self.magia)
                    print("Inteligencia: ", self.inteligencia)

            personagem = Mago(nomePersonagem, sexoPersonagem)

        personagem.exibir()
        print("Você é", personagem.nome, ", um(a)", personagem.classe ,"da terra média, onde existe um dragão que você não é nem um pouco chegado. Existem relatos de que ele te fez tropeçar uma vez no corredor da escola na frente de todos. Isso é imperdoável. Você deve fazê-lo pagar!!!")

        print("Pressione Enter para continuar")
        input()

        def Menu():
            print("Qual será seu próximo passo?")
            print("1 - Ir atrás do Dragão")
            print("2 - Treinar")

        Menu()
        
        escolha2 = int(input())

        if escolha2 == 2:
            if personagem.classe == "Guerreiro":
                dado = randint(1, 11)
                print(dado)
                if dado >= 5:
                    setattr(personagem, "forca", 110)
                    print("Força: ", personagem.forca)
                else:
                    print("Você falhou no treino, lhe falta ódio!!!")
            elif personagem.classe == "Mago":
                dado = randint(1, 10)
                print(dado)
                if dado >= 5:
                    setattr(personagem, "magia", 110)
                    print("Magia: ", personagem.magia)
                else:
                    print("Você falhou no treino, lhe falta ódio!!!")
        
        if escolha2 == 1:
            pass
        
    elif(escolha == '0'):
        vontade = 0
    
    else:
        print("Digite um número válido")