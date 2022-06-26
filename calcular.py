from random import randint

class Calcular:

    def __init__(self: object, dificuldade: int, /) -> None: # dific. somente posicional!
        
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__operacao: int = randint(1, 3)
        self.__resultado: int = self._gerar_resultado

    
    
    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade


    @property
    def valor1(self: object) -> int:
        return self.__valor1


    @property
    def valor2(self: object) -> int:
        return self.__valor2


    @property
    def operacao(self: object) -> int:
        return self.__operacao
    

    @property
    def resultado(self: object) -> int:
        return self.__resultado


    def __str__(self: object) -> str:

        op: str = ''

        if self.operacao ==1:
            op = 'Somar'
        elif self.operacao ==2:
            op = 'Subtrair'    
        elif self.operacao == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'    
        
        return f'valor1: {self.__valor1}\n valor2: {self.__valor2}\n dificuldade: {self.__dificuldade}\n operacao {op}\n'

    
    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade==1:
            return randint (0, 10)
        elif self.dificuldade==2:
            return randint(0, 100)
        elif self.dificuldade==3:
            return randint(0, 1000)
        elif self.dificuldade==4:
            return randint(10000)
        else:
            return randint(0, 100000)                

    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao==1:
            return self.valor1 + self.valor2
        elif self.operacao==2:
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2

    @property
    def _op_simbolo(self: object) -> str:
        if self.operacao==1:
            return '+'
        elif self.operacao==2:
            return '-'
        else:
            return '*'        


    def checar_resultado(self: object, resposta: int) -> bool:
        
        certo: bool = False

        if self.resultado==resposta:
            print("Resposta correta!\U0001F600")
            certo = True
        else:
            print("Resposta incorreta!\U0001F641")
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = {self.resultado}')
        return certo    


    def mostrar_operacao(self: object) -> None:
        print(f'{self.valor1} {self._op_simbolo} {self.valor2} = É com você!')

    

