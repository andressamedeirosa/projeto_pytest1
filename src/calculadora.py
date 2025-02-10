class Calculadora:
    def adicao(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b

    def fatorial(self, n):
        if n < 0:
            raise ValueError("Fatorial de número negativo não é permitido.")
        if n == 0 or n == 1:
            return 1
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def potencia(self, base, expoente):
        return base ** expoente
