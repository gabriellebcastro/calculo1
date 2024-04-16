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

def newton(f, x0, h=1e-5, max_iteracoes=1000):
    """
    Implementa o método de Newton para encontrar as raízes de uma função.
    
    Argumentos:
    f: A função para encontrar a raiz.
    x0: O valor inicial para começar a busca.
    h: A tolerância para parar a busca (default é 1e-5).
    max_iterations: O número máximo de iterações permitidas (default é 100).
    
    Retorna:
    A aproximação da raiz da função.
    """
    iteracao = 0
    while True:
        derivada_f = derivada(f, x0)
        if derivada_f == 0:
            raise ValueError("A derivada é zero no ponto x0 = {}".format(x0))
        x1 = x0 - f(x0) / derivada(f, x0)  # Fórmula do Método de Newton
        iteracao += 1
        if abs(x1 - x0) < h or iteracao >= max_iteracoes:
            break
        x0 = x1
    return x1

def arredondar(valor, casas_decimais=6):
    """
    Arredonda um valor para um número específico de casas decimais.
    
    Argumentos:
    valor: O valor a ser arredondado.
    casas_decimais: O número de casas decimais desejado.
    
    Retorna:
    O valor arredondado.
    """
    return round(valor, casas_decimais)

'''Funções
Para testar cada função, apenas retire o '#' do retorno da função desejada.
Apenas um 'return' deve ficar ativo.
'''
def funcao(x):
    '''Função Quadrática (do exemplo)'''
    #return x**2 + x 

    '''Desafio do Raimundo'''
    #return x**2-2*x
    
    '''Função Exponencial

    Para a função exponencial, escolhemos funções que
    tenha raízes reais e estão com constantes para 
    evitar derivadas nulas.'''
    #return 2**x - 1
    #return 3**x - 2
    #return 2**x-3

x_valores = [-2, -1, -1.5, -0.5, 1, 2]  # Pontos onde queremos calcular as raízes
#x_valores = [1]
for x_valor in x_valores:
    derivada_valor = derivada(funcao, x_valor)
    raizes = newton(funcao, x_valor)
    print("Para x0 =", x_valor, "o resultado da derivada é", {arredondar(derivada_valor)}, "e a raiz da função é:", {arredondar(raizes)})