def derivada(f, x, h=1e-5):
    """
    Calcula a derivada de uma função em um ponto usando diferenciação numérica.
    
    Argumentos:
    f: A função para derivar.
    x: O ponto onde calcular a derivada.
    h: O tamanho do passo para calcular a diferença finita (default é 1e-5).
    
    Retorna:
    O valor da derivada de f em x.
    """
    return (f(x + h) - f(x)) / h

def newton(f, x0, h=1e-5, max_iteracoes=100):
    """
    Implementa o método de Newton para encontrar as raízes de uma função.
    
    Argumentos:
    f: A função para encontrar a raiz.
    x0: O valor inicial para começar a busca.
    tolerance: A tolerância para parar a busca (default é 1e-5).
    max_iterations: O número máximo de iterações permitidas (default é 100).
    
    Retorna:
    A aproximação da raiz da função.
    """
    iteracao = 0
    while True:
        x1 = x0 - f(x0) / derivada(f, x0)  # Fórmula do Método de Newton
        iteracao += 1
        if abs(x1 - x0) < h or iteracao >= max_iteracoes:
            break
        x0 = x1
    return x1

#Função
def funcao(x):
    return x**2 + x 

x_valores = [-2, -1, 1, 2]  #Pontos onde queremos calcular as raízes
for x_valor in x_valores:
    derivative_value = derivada(funcao, x_valor)
    raizes = newton(funcao, x_valor)
    print("Para x =", x_valor, "o valor da derivada é", derivative_value, "e a raiz da função é:", raizes)
