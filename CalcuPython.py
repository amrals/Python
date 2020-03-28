from math import sqrt, sin, cos, tan, hypot

vontade = 1

print("##################    Seja bem vindo à CalcuPython    ##################")

while vontade == 1:

    print("Qual tipo de operação você deseja realizar?")

    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Potência")
    print("6 - Raíz quadrada")
    print("7 - Seno")
    print("8 - Cosseno")
    print("9 - Tangente")
    print("10 - Hipotenusa")
    print("0 - Sair")

    # Armazenando valor digitado pelo usuário
    Ops = int(input())

    # Condição de adição
    if Ops == 1:

        # Função de Soma, utilizando dois parâmetros, digitados pelo usuário
        def Soma(primeiroNumAdicao, segundoNumAdicao):
            resultadoSoma = primeiroNumAdicao + segundoNumAdicao
            print("O resultado é: \n")
            print(float(resultadoSoma))
        
        # Função de Soma, utilizando três parâmetros, digitados pelo usuário
        def Soma2(primeiroNumAdicao, segundoNumAdicao, terceiroNumSoma):
            resultadoSoma2 = primeiroNumAdicao + segundoNumAdicao + terceiroNumSoma
            print("O resultado é: \n")
            print(float(resultadoSoma2))

        print("Digite o primeiro número")
        primeiroNumAdicao = float(input())

        print("Digite o segundo número")
        segundoNumAdicao = float(input())

        print("Deseja adicionar mais algum número?")
        print("1 - Sim \n2 - Não \n")
        escolhaSoma = int(input())

        # Condição de escolha para adicionar mais um número à soma
        if escolhaSoma == 1:
            print("Digite o terceiro número")
            terceiroNumSoma = float(input())
            Soma2(primeiroNumAdicao, segundoNumAdicao, terceiroNumSoma)

        # Condição de manter apenas dois números na soma
        else:

            # Chamado da função, passando como parâmetro os valores obtidos pelo usuário
            Soma(primeiroNumAdicao, segundoNumAdicao)

    # Condição de subtração
    elif Ops == 2:

        # Função de Subtração, utilizando dois parâmetros, digitados pelo usuário
        def Sub(primeiroNumSub, segundoNumSub):
            resultadoSub = primeiroNumSub - segundoNumSub
            print("O resultado é: \n")
            print(float(resultadoSub))

        print("Digite o primeiro número")
        primeiroNumSub = float(input())

        print("Digite o segundo número")
        segundoNumSub = float(input())

        # Chamado da função, passando como parâmetro os valores obtidos pelo usuário
        Sub(primeiroNumSub, segundoNumSub)

    # Condição de multplicação
    elif Ops == 3:

        # Função de Multiplicação, utilizando dois parâmetros, digitados pelo usuário
        def Mul(primeiroNumMul, segundoNumMul):
            resultadoMul = primeiroNumMul * segundoNumMul
            print("O resultado é: \n")
            print(float(resultadoMul))

        print("Digite o primeiro número")
        primeiroNumMul = float(input())

        print("Digite o segundo número")
        segundoNumMul = float(input())

        # Chamado da função, passando como parâmetro os valores obtidos pelo usuário
        Mul(primeiroNumMul, segundoNumMul)

    # Condição de divisão
    elif Ops == 4:

        # Função de Divisão, utilizando dois parâmetros, digitados pelo usuário
        def Div(primeiroNumDiv, segundoNumDiv):
            resultadoDiv = primeiroNumDiv / segundoNumDiv
            print("O resultado é: \n")
            print(float(resultadoDiv))

        print("Digite o primeiro número")
        primeiroNumDiv = float(input())

        print("Digite o segundo número diferente de 0")
        segundoNumDiv = float(input())

        try:
            Div(primeiroNumDiv, segundoNumDiv)

        except ZeroDivisionError:
            print("Você não pode dividir um número por zero")
    
    # Condição de potência
    elif Ops == 5:

        # Função de Potência, utilizando dois parâmetros, digitados pelo usuário
        def Pot(primeiroNumPot, segundoNumPot):
            resultadoPot = primeiroNumPot ** segundoNumPot
            print("O resultado é: \n")
            print(float(resultadoPot))
        
        print("Digite o primeiro número")
        primeiroNumPot = float(input())

        print("Digite o segundo número")
        segundoNumPot = float(input())

        # Chamado da função, passando como parâmetro os valores obtidos pelo usuário
        Pot(primeiroNumPot, segundoNumPot)
    
    # Condição de raíz
    elif Ops == 6:

        # Função de Raíz, utilizando um parâmetro, digitado pelo usuário
        def Sqrt(numeroRaiz):
            resultadoSqrt = sqrt(numeroRaiz)
            print("O resultado é: \n")
            print(resultadoSqrt)
        
        print("Digite um número pra saber sua raíz quadrada")
        numeroRaiz = float(input())

        # Chamado da função, passando como parâmetro o valor obtido pelo usuário
        Sqrt(numeroRaiz)
    
    # Condição de seno
    elif Ops == 7:

        # Função de Seno, utilizando um parâmetro, digitado pelo usuário
        def Sen(numeroSeno):
            resultadoSeno = sin(numeroSeno)
            print("O resultado é: \n")
            print(resultadoSeno)

        print("Digite um número para saber o seno dele")
        numeroSeno = float(input())
        
        # Chamado da função, passando um parâmetro, digitado pelo usuário
        Sen(numeroSeno)

    # Condição de cosseno
    elif Ops == 8:

        # Função de Cosseno, utilizando um parâmetro, digitado pelo usuário
        def Cos(numeroCos):
            resultadoCos = cos(numeroCos)
            print("O resultado é: \n")
            print(resultadoCos)

        print("Digite um número para saber o cosseno dele")
        numeroCos = float(input())
        
        # Chamado da função, passando um parâmetro, digitado pelo usuário
        Cos(numeroCos)
    
    # Condição de tangente
    elif Ops == 9:

        # Função de Tangente, utilizando um parâmetro, digitado pelo usuário
        def Tan(numeroTan):
            resultadoTan = tan(numeroTan)
            print("O resultado é: \n")
            print(resultadoTan)

        print("Digite um número para saber o cosseno dele")
        numeroTan = float(input())
        
        # Chamado da função, passando um parâmetro, digitado pelo usuário
        Tan(numeroTan)

    # Condição de hipotenusa
    elif Ops == 10:

        # Função de Hipotenusa, utilizando dois parâmetros, digitados pelo usuário
        def Hip(primeiroNumHip, segundoNumHip):
            resultadoHip = hypot(primeiroNumHip, segundoNumHip)
            print("O resultado é: \n")
            print(resultadoHip)

        print("Digite um cateto")
        primeiroNumHip = float(input())

        print("Digite outro cateto")
        segundoNumHip = float(input())
        
        # Chamado da função, passando dois parâmetros, digitados pelo usuário
        Hip(primeiroNumHip, segundoNumHip)


    # Condição de saída
    elif Ops == 0:

        # Definindo a condicional para sair do loop
        vontade = 2