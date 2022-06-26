from calcular import Calcular

def main() -> None:
    
    pontos: int = 0
    jogar(pontos)

def jogar(pontos: int) -> None:
    dificuldade: int = int(input('Informe o nível de dificuldade: [1] [2] [3] [4] '))
        
    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado = int(input())

    if calc.checar_resultado(resultado):
        pontos+=1
        print(f'Voce tem {pontos} pontos!')

    continuar = int(input('Deseja continuar [1](sim) [0](não): '))

    if continuar:
        jogar(pontos)
    else:
        print(f'\U0001F9E0 Você finalizou com {pontos} pontos!')
        print('Jogo finalizado...\U0001F480		')    


if __name__=="__main__":
    main()



