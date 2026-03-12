#PROJETO 2
#GUILHERME FELICIANO MARQUES IST1113868
def cria_posicao(col, lin):
    '''
    função: recebe um caracter e um inteiro correspondentes à coluna
col e à linha lin e devolve a posição correspondente. O construtor verifica
2A representação interna dos elementos do tipo deve ser imutável e hashable.
a validade dos seus argumentos, gerando um ValueError com a mensagem
'cria_posicao: argumentos invalidos' caso os seus argumentos não sejam válidos
    argumentos: coluna e linha correspondentes à posição'''
    # Verifica se 'lin' é um inteiro entre 1 e 10 e 'col' é uma string entre 'a' e 'j'
    if type(lin) == int and lin in range(1, 11) and type(col) == str and col in ('abcdefghij'):
        # Retorna a posição como um tuplo (col, lin)
        return (col, lin)
    else:
        # Levanta um erro se os argumentos forem inválidos
        raise ValueError("cria_posicao: argumentos invalidos")

def obtem_pos_col(pos):
    '''
    função: devolve a coluna col da posição p.
    argumentos: posição'''
    # Verifica se a posição é uma string
    if type(pos) == str:
        # Itera sobre cada caractere na string
        for i in pos:
            # Verifica se o caractere está entre 'a' e 'j'
            if i in ('abcdefghij'):
                # Retorna o caractere que representa a coluna
                return i
    # Verifica se a posição é um tuplo
    elif type(pos) == tuple:
        # Retorna o primeiro elemento do tuplo que representa a coluna
        return pos[0]

def obtem_pos_lin(pos):
    '''
    função: devolve a linha lin da posição p.
    argumentos: posição'''
    # Verifica se a posição é uma string
    if type(pos) == str:
        # Itera sobre cada caractere na string
        for i in pos:
            # Verifica se o caractere está entre 1 e 10
            if i in range(1, 11):
                # Retorna o caractere que representa a linha
                return i
    # Verifica se a posição é um tuplo
    elif type(pos) == tuple:
        # Retorna o segundo elemento do tuplo que representa a linha
        return pos[1]

def eh_posicao(pos):
    '''
    função: devolve True caso o seu argumento seja um TAD posicao e
False caso contrário.
    argumentos: posição'''
    # Verifica se a posição é um tuplo com dois elementos
    if type(pos) == tuple and len(pos) == 2 and pos[0] in 'abcdefghij' and pos[1] in range(1, 11):
        return True
    # Verifica se a posição é uma string com 2 ou 3 caracteres
    elif type(pos) == str and len(pos) in (2, 3) and pos[0] in 'abcdefghij':
        lin = pos[1:]  # Obtém a parte numérica da string
        # Verifica se a parte numérica é um dígito e está no intervalo de 1 a 10
        return lin.isdigit() and int(lin) in range(1, 11)
    return False  # Retorna False se nenhuma das condições acima for satisfeita

def posicoes_iguais(p1, p2):
    '''
    função:  devolve True apenas se p1 e p2 são posições e são
iguais, e False caso contrário.
    argumentos: posições'''
    # Verifica se ambas as posições são válidas e se são iguais
    if eh_posicao(p1) and eh_posicao(p2) and p1 == p2:
        return True
    return False

def posicao_para_str(pos):
    '''
    função:  devolve a cadeia de caracteres que representa o seu argumento, como mostrado nos exemplos.
    argumentos: posição'''
    # Verifica se a posição é válida
    if eh_posicao(pos):
        # Concatena a coluna e a linha da posição em uma string e retorna
        return str(pos[0]) + str(pos[1])

def str_para_posicao(string):
    '''
    função: devolve a posição representada pelo seu argumento
    argumentos: string da posição'''
    # Inicializa um tupl0 vazia para armazenar a posição
    r = ()
    # Define as letras válidas para a coluna
    letras = ('abcdefghijjlmnopqrstuvwxyz')
    # Verifica se a string representa uma posição válida
    if eh_posicao(string):
        # Verifica se a string é do tipo str
        if type(string) == str:
            # Itera sobre cada caractere na string
            for i in string:
                # Verifica se o caractere está nas letras válidas
                if i in letras:
                    # Define a coluna como o caractere encontrado
                    col = i
            # Itera sobre cada caractere na string novamente
            for j in string:
                # Adiciona o caractere ao tuplo r
                r += (j,)
            # Verifica se a string tem 2 caracteres
            if len(string) == 2:
                # Define a linha como o segundo caractere convertido para inteiro
                lin = int(r[1])
            else:
                # Define a linha como a concatenação do segundo e terceiro caracteres convertidos para inteiro
                lin = int(str(r[1])+str(r[2]))
        # Retorna a posição como um tuplo (col, lin)
        return (col, lin)
    else:
        # Retorna None se a string não representar uma posição válida
        return None

def obtem_tabuleiro(n): #função adicional
    '''
    função: devolve um tabuleiro quadrado de dimensão n*2 x n*2, com todas as posições vazias.
    argumentos: quantidade de órbitas que o tabuleiro tem(n)'''
    # Inicializa uma lista vazia para armazenar as linhas do tabuleiro
    tuplo = []
    # Itera sobre o número de linhas do tabuleiro (n*2)
    for i in range(n*2):
        # Inicializa uma lista vazia para armazenar os valores de cada linha
        linha = []
        # Itera sobre o número de colunas do tabuleiro (n*2)
        for j in range(n*2):
            # Adiciona o valor 0 (representando uma posição vazia) à linha
            linha.append(0)
        # Adiciona a linha completa à lista do tabuleiro
        tuplo.append((linha))
    # Retorna o tabuleiro completo como uma lista de listas
    return (tuplo)

def eh_posicao_valida(pos, n):
    '''
    função: devolve True se p é uma posição válida dentro do tabuleiro
de Orbito-n e False caso contrário.
    argumentos: posição e quantidade de órbitas do tabuleiro'''
    # Verifica se a posição é válida
    if not eh_posicao(pos):
        return False
    # Obtém a coluna da posição
    col = obtem_pos_col(pos)
    # Obtém a linha da posição
    lin = obtem_pos_lin(pos)
    # Verifica se a coluna está dentro do intervalo permitido e se a linha está dentro do intervalo permitido
    return col in 'abcdefghij'[:n*2] and 1 <= lin <= n*2

def obtem_coordenadas(posicao): #função adicional
    '''
    função: devolve um tuplo com as coordenadas da posição
    argumentos: posição'''
    # Define as letras válidas para a coluna
    letras = ('abcdefghij')
    # Itera sobre as letras para encontrar a coluna correspondente
    for i in letras:
        if i == str(posicao[0]):
            # Obtém o índice da coluna
            y = letras.index(i)
    # Retorna a linha (ajustada para índice 0) e a coluna
    return (posicao[1]-1, y)

def obtem_posicoes_adjacentes(pos, n, d):
    '''
    função: devolve um tuplo com as posições do tabuleiro
de Orbito-n adjacentes à posição p se d é True, ou as posições adjacentes ortogonais
se d é False. As posições do tuplo são ordenadas em sentido horário começando
pela posição acima de p.
    argumentos: posição, quantidade de órbitas do tabuleiro e booleano(True ou False)'''
    # Verifica se a posição é válida
    if eh_posicao_valida(pos, n):
        adjacentes_diagonais = ()  # Inicializa um tuplo vazia para armazenar as posições adjacentes diagonais
        adjacentes_ortogonais = ()  # Inicializa um tuplo vazia para armazenar as posições adjacentes ortogonais
        lin = obtem_pos_lin(pos)  # Obtém a linha da posição
        lin_inicial = lin  # Armazena a linha inicial
        lin_2 = lin  # Inicializa uma variável para manipulação da linha
        letras = ('abcdefghijklmnopqrstuvwxyz')  # Define as letras válidas para a coluna
        (_, col) = obtem_coordenadas(pos)  # Obtém a coluna da posição
        col_inicial = col  # Armazena a coluna inicial
        col_2 = col  # Inicializa uma variável para manipulação da coluna

        # Se d for False, calcula as posições adjacentes ortogonais
        if d == False:
            col = col_inicial  # Reseta a coluna para a inicial
            lin = lin_inicial  # Reseta a linha para a inicial
            # Verifica e adiciona a posição acima
            if eh_posicao_valida((letras[col], lin - 1), n):
                adjacentes_ortogonais += ((letras[col], lin - 1),)
            # Verifica e adiciona a posição à direita
            if col + 1 < len(letras) and eh_posicao_valida((letras[col + 1], lin), n):
                adjacentes_ortogonais += ((letras[col + 1], lin),)
            # Verifica e adiciona a posição abaixo
            if eh_posicao_valida((letras[col], lin + 1), n):
                adjacentes_ortogonais += ((letras[col], lin + 1),)
            # Verifica e adiciona a posição à esquerda
            if col - 1 >= 0 and eh_posicao_valida((letras[col - 1], lin), n):
                adjacentes_ortogonais += ((letras[col - 1], lin),)
            return adjacentes_ortogonais  # Retorna as posições adjacentes ortogonais

        # Se d for True, calcula as posições adjacentes diagonais
        if d == True:
            col_2 = col_inicial  # Reseta a coluna para a inicial
            lin_2 = lin_inicial  # Reseta a linha para a inicial
            # Move para a posição acima
            while lin_2 > 1 and lin_2 > lin_inicial - 1:
                lin_2 -= 1
            # Adiciona a posição acima e acima à direita
            while col_2 < col_inicial + 2:
                if (letras[col_2], lin_2) != pos and eh_posicao_valida((letras[col_2], lin_2), n):
                    adjacentes_diagonais += ((letras[col_2], lin_2),)
                col_2 += 1

            col_2 = col_inicial  # Reseta a coluna para a inicial
            lin_2 = lin_inicial  # Reseta a linha para a inicial
            # Move para a posição à direita
            while col_2 < n * 2 and col_2 < col_inicial + 1:
                col_2 += 1
            if col_2 < len(letras) and eh_posicao_valida((letras[col_2], lin_2), n) and (letras[col_2], lin_2) != pos and (letras[col_2], lin_2) not in adjacentes_diagonais:
                adjacentes_diagonais += ((letras[col_2], lin_2),)

            col_2 = col_inicial  # Reseta a coluna para a inicial
            lin_2 = lin_inicial  # Reseta a linha para a inicial
            # Move para a diagonal inferior direita
            while col_2 < n * 2 and col_2 < col_inicial + 1:
                col_2 += 1
            while lin_2 < n * 2 and lin_2 < lin_inicial + 1:
                lin_2 += 1

            while col_2 > col_inicial - 2:
                if col_2 >= 0 and col_2 < len(letras) and (letras[col_2], lin_2) != pos and eh_posicao_valida((letras[col_2], lin_2), n) and (letras[col_2], lin_2) not in adjacentes_diagonais:
                    adjacentes_diagonais += ((letras[col_2], lin_2),)
                col_2 -= 1

            col_2 = col_inicial  # Reseta a coluna para a inicial
            lin_2 = lin_inicial  # Reseta a linha para a inicial
            # Move para a posição à esquerda
            while col_2 > 0 and col_2 > col_inicial - 1:
                col_2 -= 1

            if col_2 >= 0 and eh_posicao_valida((letras[col_2], lin_2), n) and (letras[col_2], lin_2) != pos and (letras[col_2], lin_2) not in adjacentes_diagonais:
                adjacentes_diagonais += ((letras[col_2], lin_2),)

            col_2 = col_inicial  # Reseta a coluna para a inicial
            lin_2 = lin_inicial  # Reseta a linha para a inicial
            # Move para a diagonal superior esquerda
            while col_2 > 0 and col_2 > col_inicial - 1:
                col_2 -= 1
            while lin_2 > 1 and lin_2 > lin_inicial - 1:
                lin_2 -= 1

            if col_2 >= 0 and eh_posicao_valida((letras[col_2], lin_2), n) and (letras[col_2], lin_2) != pos and (letras[col_2], lin_2) not in adjacentes_diagonais:
                adjacentes_diagonais += ((letras[col_2], lin_2),)
            return adjacentes_diagonais  # Retorna as posições adjacentes diagonais

def ordena_posicoes_tabuleiro(n): #função adicional
    '''
    função: devolve um tuplo com todas as posições do tabuleiro de Orbito-n ordenadas
    argumentos: quantidade de órbitas do tabuleiro'''
    letras = ('abcdefghij')  # Define as letras válidas para as colunas
    posicoes = ()  # Inicializa um tuplo vazio para armazenar as posições
    c = 0  # Inicializa um contador
    c2 = 1  # Inicializa um contador
    tab = obtem_tabuleiro(n)  # Obtém um tabuleiro vazio de tamanho n
    col = (n*2//2)-1  # Calcula a coluna inicial
    lin = n*2//2  # Calcula a linha inicial
    c_lin = 1  # Inicializa um contador para linhas
    c_col = 0  # Inicializa um contador para colunas
    c_col_1 = 1  # Inicializa um contador para colunas
    c_c = 3  # Inicializa um contador
    c_lin_0 = 0  # Inicializa um contador para linhas
    c2 = 2  # Inicializa um contador

    # Adiciona as posições centrais do tabuleiro
    if n >= 1:
        if eh_posicao_valida(cria_posicao(letras[len(tab)//2-1],len(tab[0])//2),n):
            posicoes += (cria_posicao(letras[len(tab)//2-1],len(tab[0])//2),)
        if eh_posicao_valida(cria_posicao(letras[len(tab)//2],len(tab[0])//2),n):
            posicoes += (cria_posicao(letras[len(tab)//2],len(tab[0])//2),)
        if eh_posicao_valida(cria_posicao(letras[len(tab)//2],len(tab[0])//2+1),n):
            posicoes += (cria_posicao(letras[len(tab)//2],len(tab[0])//2+1),)
        if eh_posicao_valida(cria_posicao(letras[len(tab)//2-1],len(tab[0])//2+1),n):
            posicoes += (cria_posicao(letras[len(tab)//2-1],len(tab[0])//2+1),)

    # Adiciona as posições adjacentes às centrais
    if n >= 2:
        while c2 <= n:
            c = 0
            col = (n*2//2)-1  # Reseta a coluna para a inicial
            lin = n*2//2  # Reseta a linha para a inicial
            posicoes += (cria_posicao(letras[col-c_col_1], lin-c_lin),)  # Adiciona a posição à esquerda superior

            c = 0
            col -= c_col  # Ajusta a coluna
            while c < c_c:
                posicoes += (cria_posicao(letras[col], lin-c_lin),)  # Adiciona as posições à esquerda
                col += 1
                c += 1

            c = 0
            col -= 1
            lin -= c_lin_0  # Ajusta a linha
            while c < c_c:
                if cria_posicao(letras[col], lin) not in posicoes:
                    posicoes += (cria_posicao(letras[col], lin),)  # Adiciona as posições abaixo
                    lin += 1
                    c += 1

            c = 0
            while c < c_c:
                if cria_posicao(letras[col-1], lin-1) not in posicoes:
                    posicoes += (cria_posicao(letras[col-1], lin-1),)  # Adiciona as posições à direita inferior
                col -= 1
                c += 1

            c = 0
            while c < c_c:
                if cria_posicao(letras[col], lin-1) not in posicoes:
                    posicoes += (cria_posicao(letras[col], lin-1),)  # Adiciona as posições acima
                lin -= 1
                c += 1

            # Ajusta os contadores para a próxima iteração
            c_lin += 1
            c_col += 1
            c_c += 2
            c_lin_0 += 1
            c_col_1 += 1
            c2 += 1

    return posicoes  # Retorna o tuplo com as posições ordenadas

def obtem_posicoes_ordenadas_orbitas(n): #função adicional
    '''
    função: devolve um tuplo de tuplos com as posições do tabuleiro de Orbito-n ordenadas por órbitas
    argumentos: quantidade de órbitas do tabuleiro'''
    # Obtém todas as posições ordenadas do tabuleiro
    posicoes = ordena_posicoes_tabuleiro(n)
    orbitas = []  # Inicializa uma lista para armazenar as órbitas
    inicio = 0  # Define o índice inicial
    incremento = 4  # Define o incremento inicial

    # Enquanto o índice inicial for menor que o número de posições
    while inicio < len(posicoes):
        fim = inicio + incremento  # Calcula o índice final da órbita atual
        # Adiciona a órbita atual à lista de órbitas
        orbitas.append(tuple(posicoes[inicio:fim]))
        inicio = fim  # Atualiza o índice inicial para a próxima órbita
        incremento += 8  # Aumenta o incremento para a próxima órbita

    # Retorna as órbitas como um tuplo de tuplos
    return tuple(orbitas)

def obtem_orbita_posicao(n, posicao): #função adicional
    '''
    função: devolve o índice da órbita a que a posição p pertence, ou None caso a posição não pertença a nenhuma órbita
    argumentos: quantidade de órbitas do tabuleiro e posição'''
    # Obtém as órbitas ordenadas do tabuleiro de tamanho n
    orbitas = obtem_posicoes_ordenadas_orbitas(n)
    # Itera sobre cada órbita e seu índice
    for indice_orbita, orbita in enumerate(orbitas):
        # Verifica se a posição está na órbita atual
        if posicao in orbita:
            # Retorna o índice da órbita onde a posição foi encontrada
            return indice_orbita
    # Retorna None se a posição não estiver em nenhuma órbita
    return None

def ordena_posicoes_por_leitura(n): #função adicional
    '''
    função: devolve um tuplo com todas as posições do tabuleiro de Orbito-n ordenadas por leitura
    argumentos: quantidade de órbitas do tabuleiro'''
    # Obtém as órbitas ordenadas do tabuleiro de tamanho n
    orbitas = obtem_posicoes_ordenadas_orbitas(n)
    # Define uma função lambda para ordenar as posições primeiro pela linha (pos[1]) e depois pela coluna (pos[0])
    posicao_ordenacao = lambda pos: (pos[1], pos[0])
    posicoes_ordenadas = ()  # Inicializa um tuplo vazio para armazenar as posições ordenadas
    # Itera sobre cada órbita
    for orbita in orbitas:
        # Ordena as posições na órbita usando a função lambda e adiciona ao tuplo de posições ordenadas
        posicoes_ordenadas += tuple(sorted(orbita, key=posicao_ordenacao))
    return posicoes_ordenadas  # Retorna o tuplo com as posições ordenadas

def ordena_posicoes(tuplo, n):
    '''
    função: devolve um tuplo de posições com as mesmas posições de t
ordenadas de acordo com a ordem de leitura do tabuleiro de Orbito-n.
    argumentos: tuplo de posições e quantidade de órbitas do tabuleiro
'''
    # Obtém as posições ordenadas por leitura para o tabuleiro de tamanho n
    posicoes_ordenadas = ordena_posicoes_por_leitura(n)
    # Retorna um tuplo com as posições que estão em 'tuplo' e também em 'posicoes_ordenadas'
    return tuple(pos for pos in posicoes_ordenadas if pos in tuplo)

def cria_pedra_branca():
    '''
    função: devolve uma pedra pertencente ao jogador branco.
    argumentos: nenhum'''
    # Retorna o valor -1, que representa uma pedra branca
    return -1

def cria_pedra_preta():
    '''
    função: devolve uma pedra pertencente ao jogador preto.
    argumentos: nenhum'''
    # Retorna o valor 1, que representa uma pedra preta
    return 1

def cria_pedra_neutra():
    '''
    função: devolve uma pedra neutra.
    argumentos: nenhum'''
    # Retorna o valor " ", que representa uma pedra neutra
    return " "

def eh_pedra(pedra):
    '''
    função: devolve True caso o seu argumento seja um TAD pedra e False
caso contrário.
    argumentos: pedra
'''
    # Verifica se a pedra é uma pedra branca, preta, neutra ou uma representação em string ('X', 'O', '')
    if pedra in (cria_pedra_branca(), cria_pedra_preta(), cria_pedra_neutra(), 'X', 'O', ''):
        return True
    else:
        return False

def eh_pedra_branca(pedra):
    '''
    função: devolve True caso a pedra p seja do jogador branco e False
caso contrário.
    argumentos: pedra
'''
    # Verifica se a pedra é uma pedra branca ou a representação em string 'O'
    if pedra in (cria_pedra_branca(), 'O'):
        return True
    return False

def eh_pedra_preta(pedra):
    '''
    função: devolve True caso a pedra p seja do jogador preto e False
caso contrário.
    argumentos: pedra'''
    # Verifica se a pedra é uma pedra preta ou a representação em string 'X'
    if pedra in (cria_pedra_preta(), 'X'):
        return True
    return False

def pedras_iguais(p1, p2):
    '''
    função: devolve True apenas se p1 e p2 são pedras e são iguais.~
    argumentos: pedras'''
    # Verifica se as duas pedras são diferentes
    if p1 != p2:
        return False  # Retorna False se as pedras forem diferentes
    return True  # Retorna True se as pedras forem iguais

def pedra_para_str(pedra):
    '''
    função:  devolve a cadeia de caracteres que representa o jogador dono
da pedra, isto é, 'O', 'X' ou ' ' para pedras do jogador branco, preto ou
neutra respetivamente.
    argumentos: pedra'''
    # Verifica se a pedra é uma pedra preta
    if pedra == cria_pedra_preta():
        # Retorna a string 'X' para a pedra preta
        return str('X')
    # Verifica se a pedra é uma pedra branca
    elif pedra == cria_pedra_branca():
        # Retorna a string 'O' para a pedra branca
        return str('O')
    # Verifica se a pedra é uma pedra neutra
    elif pedra == cria_pedra_neutra():
        # Retorna a string " " para a pedra neutra
        return " "

def eh_pedra_jogador(pedra):
    '''
    função:  devolve True caso a pedra p seja de um jogador e False caso
contrário.
    argumentos: pedra'''
    # Verifica se a pedra é uma pedra válida
    if eh_pedra(pedra):
        # Verifica se a pedra é uma pedra branca ou preta
        if eh_pedra_branca(pedra) or eh_pedra_preta(pedra):
            return True
    return False
def pedra_para_int(pedra):
    '''
    função:  devolve um inteiro valor 1, -1 ou 0, dependendo se a pedra é do
jogador preto, branco ou neutra, respetivamente.
    argumentos: pedra'''
    # Verifica se a pedra é preta
    if eh_pedra_preta(pedra):
        # Retorna 1 para pedra preta
        return 1
    # Verifica se a pedra é branca
    elif eh_pedra_branca(pedra):
        # Retorna -1 para pedra branca
        return -1
    # Verifica se a pedra é neutra
    elif pedra == cria_pedra_neutra():
        # Retorna 0 para pedra neutra
        return 0

def cria_tabuleiro_vazio(n):
    '''
    função:  devolve um tabuleiro de Orbito com n órbitas, sem
posições ocupadas. O construtor verifica a validade do argumento, gerando
um ValueError com a mensagem 'cria_tabuleiro_vazio: argumento inv
alido' caso os seu argumento não seja válido. Considere que o número
mínimo de órbitas de um tabuleiro de Orbito é 2 e o máximo 5.
    argumentos: quantidade de órbitas do tabuleiro'''
    # Verifica se o valor de 'n' está no intervalo permitido (2 a 5)
    if n in range(2, 6):
        # Retorna um tabuleiro vazio de tamanho 'n*2xn*2'
        return obtem_tabuleiro(n)
    # Levanta um erro se o valor de 'n' for inválido
    raise ValueError("cria_tabuleiro_vazio: argumento invalido")

def cria_tabuleiro(n, tp, tb):
    '''
    função: devolve um tabuleiro de Orbito com n órbitas, com as
posições do tuplo tp ocupadas por pedras pretas e as posições do tuplo 
tb ocupadas por pedras brancas. O construtor verifica a validade dos argumentos,
gerando um ValueError com a mensagem 'cria_tabuleiro: argumentos i
nvalidos' caso os seus argumentos não sejam válidos. Considere que o
número mínimo de órbitas de um tabuleiro de Orbito é 2 e o máximo 5.
    argumentos: quantidade de órbitas do tabuleiro, tuplo de posições ocupadas por pedras pretas e tuplo de posições ocupadas por pedras brancas'''
    # Verifica se 'n' é um inteiro entre 2 e 5, 'tp' e 'tb' são tuplos, todas as posições em 'tp' e 'tb' são válidas,
    # não há posições duplicadas em 'tp' e 'tb', e as posições em 'tp' e 'tb' não se sobrepõem
    if type(n) == int and 2 <= n <= 5 and type(tp) == tuple and type(tb) == tuple and all(eh_posicao(pos) for pos in tp) and all(eh_posicao_valida(pos, n) for pos in tp) and all(eh_posicao_valida(pos, n) for pos in tb) and not any(pos in tb for pos in tp) and not any(pos in tp for pos in tb) and len(tp) == len(set(tp)) and len(tb) == len(set(tb)) and all(type(pos[0]) == str and pos[0] in 'abcdefghij' and type(pos[1]) == int and 1 <= pos[1] <= 10 for pos in tp) and all(type(pos[0]) == str and pos[0] in 'abcdefghij' and type(pos[1]) == int and 1 <= pos[1] <= 10 for pos in tb):
        lista = cria_tabuleiro_vazio(n)  # Cria um tabuleiro vazio de tamanho 'n*2 x n*2'
        for i in tp:
            (y, g) = obtem_coordenadas(i)  # Obtém as coordenadas da posição 'i' em 'tp'
            lista[y][g] = 1  # Coloca uma pedra preta na posição 'i'
        for i in tb:
            (y, g) = obtem_coordenadas(i)  # Obtém as coordenadas da posição 'i' em 'tb'
            lista[y][g] = -1  # Coloca uma pedra branca na posição 'i'
        return lista  # Retorna o tabuleiro com as pedras colocadas
    else:
        raise ValueError("cria_tabuleiro: argumentos invalidos")  # Levanta um erro se os argumentos forem inválidos
    
def cria_copia_tabuleiro(tab):
    '''
    função: recebe um tabuleiro e devolve uma cópia do tabuleiro.
    argumentos: tabuleiro'''
    # Inicializa uma lista vazia para armazenar a cópia do tabuleiro
    tab_copia = []
    # Itera sobre cada linha do tabuleiro original
    for i in tab:
        # Adiciona uma cópia da linha à lista de cópia do tabuleiro
        tab_copia.append(i.copy())
    # Retorna a cópia do tabuleiro
    return tab_copia

def obtem_numero_orbitas(tab): #função adicional
    '''
    função: devolve o número de órbitas do tabuleiro.
    argumentos: tabuleiro'''
    # Retorna o número de órbitas no tabuleiro, que é metade do tamanho do tabuleiro
    return len(tab) / 2

def obtem_pedra(tab, pos):
    '''
    função: devolve a pedra na posição p do tabuleiro t. Se a posição
não estiver ocupada, devolve uma pedra neutra.
    argumentos: tabuleiro e posição'''
    # Obtém as coordenadas (linha, coluna) da posição fornecida
    (y, g) = obtem_coordenadas(pos)
    
    # Verifica o valor na posição do tabuleiro e retorna a pedra correspondente
    if tab[y][g] == 1:
        return cria_pedra_preta()  # Retorna uma pedra preta se o valor for 1
    elif tab[y][g] == -1:
        return cria_pedra_branca()  # Retorna uma pedra branca se o valor for -1
    elif tab[y][g] == 0:
        return cria_pedra_neutra()  # Retorna uma pedra neutra se o valor for 0

def obtem_linha_horizontal(tab, pos):
    '''
    função: devolve o tuplo formado por tuplos de dois elementos correspondentes à posicao e o valor de todas as posições da linha
horizontal que passa pela posição p, ordenadas de esquerda para a direita.
    argumentos: tabuleiro e posição'''
    # Obtém a linha da posição fornecida
    lin, _ = obtem_coordenadas(pos)
    # Retorna um tuplo de posições e pedras na linha horizontal da posição fornecida
    return tuple((cria_posicao('abcdefghij'[i], lin + 1), obtem_pedra(tab, cria_posicao('abcdefghij'[i], lin + 1)))for i in range(len(tab[0])))


def obtem_linha_vertical(tab, pos):
    '''
    função: devolve o tuplo formado por tuplos de dois elementos correspondentes à posicao e o valor de todas as posições da linha vertical
que passa pela posição p, ordenadas de cima para a baixo.
    argumentos: tabuleiro e posição'''
    # Obtém a coluna da posição fornecida
    col = obtem_pos_col(pos)
    # Retorna um tuplo de posições e pedras na coluna vertical da posição fornecida
    return tuple((cria_posicao(col, i + 1), obtem_pedra(tab, cria_posicao(col, i + 1))) for i in range(len(tab)))

def obtem_linhas_diagonais(tab, pos):
    '''
    função: devolve dois tuplos formados cada um deles por
tuplos de dois elementos correspondentes à posicao e o valor de todas as
posições que formam a diagonal (descendente da esquerda para a direita ) e
antidiagonal (ascendente da esquerda para a direita) que passam pela posição
p, respetivamente.
    argumentos: tabuleiro e posição'''
    r = ()  # Inicializa um tuplo vazia para armazenar a linha diagonal descendente
    r2 = ()  # Inicializa um tuplo vazia para armazenar a linha diagonal ascendente
    (lin, col) = obtem_coordenadas(pos)  # Obtém as coordenadas (linha, coluna) da posição fornecida
    col_inicial = col  # Armazena a coluna inicial
    lin_inicial = lin  # Armazena a linha inicial
    letras = ('abcdefghij')  # Define as letras válidas para as colunas

    # Move para o canto superior esquerdo da diagonal descendente
    while col > 0 and lin > 0:
        col -= 1
        lin -= 1

    # Percorre a diagonal descendente e armazena as posições e pedras
    while len(r) < len(tab) and col < len(tab) and lin < len(tab):
        posicao = cria_posicao(letras[col], lin + 1)  # Cria a posição
        pedra = obtem_pedra(tab, posicao)  # Obtém a pedra na posição
        r += ((posicao, pedra),)  # Adiciona a posição e pedra ao tuplo
        col += 1
        lin += 1

    col = col_inicial  # Reseta a coluna para a inicial
    lin = lin_inicial  # Reseta a linha para a inicial

    # Move para o canto inferior esquerdo da diagonal ascendente
    while col > 0 and lin < len(tab) - 1:
        col -= 1
        lin += 1

    # Percorre a diagonal ascendente e armazena as posições e pedras
    while len(r2) < len(tab) and col < len(tab) and lin >= 0:
        posicao = cria_posicao(letras[col], lin + 1)  # Cria a posição
        pedra = obtem_pedra(tab, posicao)  # Obtém a pedra na posição
        r2 += ((posicao, pedra),)  # Adiciona a posição e pedra ao tuplo
        col += 1
        lin -= 1

    return (r, r2)  # Retorna os tuplos com as posições e pedras das diagonais

def obtem_posicoes_pedra(tab, jog):
    '''
    função: devolve o tuplo formado por todas as posições do
tabuleiro ocupadas por pedras j (brancas, pretas ou neutras), ordenadas em
ordem de leitura do tabuleiro
    argumentos: tabuleiro e pedra'''
    r = ()  # Inicializa um tuplo vazio para armazenar as posições das pedras
    letras = ('abcdefghij')  # Define as letras válidas para as colunas
    # Itera sobre cada linha do tabuleiro
    for lin, linha in enumerate(tab):
        # Itera sobre cada valor na linha
        for col, valor in enumerate(linha):
            # Verifica se o valor corresponde à pedra do jogador
            if (jog == cria_pedra_preta() and valor == 1) or (jog == cria_pedra_branca() and valor == -1) or (jog == cria_pedra_neutra() and valor == 0):
                # Adiciona a posição da pedra ao tuplo
                r += (cria_posicao(letras[col], lin + 1),)
    # Retorna as posições das pedras ordenadas
    return ordena_posicoes(r, len(tab) // 2)

def coloca_pedra(tab, pos, jog):
    '''
    função: modifica destrutivamente o tabuleiro t colocando a pedra
j na posição p, e devolve o próprio tabuleiro.
    argumentos: tabuleiro, posição e pedra'''
    # Obtém as coordenadas (linha, coluna) da posição fornecida
    y, g = obtem_coordenadas(pos)
    
    # Converte a pedra do jogador para seu valor inteiro correspondente e coloca no tabuleiro
    tab[y][g] = pedra_para_int(jog)
    
    # Retorna o tabuleiro atualizado
    return tab

def remove_pedra(tab, pos):
    '''
    função:  modifica destrutivamente o tabuleiro p removendo a pedra
da posição p, e devolve o próprio tabuleiro
    argumentos: tabuleiro e posição'''
    # Obtém as coordenadas (linha, coluna) da posição fornecida
    (y, g) = obtem_coordenadas(pos)
    
    # Define o valor da posição no tabuleiro como 0 (representando uma posição vazia)
    tab[y][g] = 0
    
    # Retorna o tabuleiro atualizado
    return tab

def eh_tabuleiro(tab):
    '''
    função: devolve True caso o seu argumento seja um TAD tabuleiro
e False caso contrário.
    argumento: tabuleiro'''
    # Verifica se 'tab' é uma lista e se todos os elementos de 'tab' são listas
    if isinstance(tab, list) and all(isinstance(linha, list) for linha in tab):
        tamanho = len(tab)  # Obtém o tamanho de 'tab'
        # Verifica se o tamanho de 'tab' está entre 4 e 10 e se todas as linhas têm o mesmo tamanho
        if 4 <= tamanho <= 10 and all(len(linha) == tamanho for linha in tab):
            # Verifica se todos os elementos em 'tab' são -1, 0 ou 1
            return all(elemento in (-1, 0, 1) for linha in tab for elemento in linha)
    return False  # Retorna False se alguma das condições acima não for satisfeita

def tabuleiros_iguais(t1, t2):
    '''
    função: devolve True apenas se t1 e t2 forem tabuleiros e
forem iguais.
    argumentos: tabuleiros'''
    # Verifica se os tabuleiros têm o mesmo número de linhas e colunas
    if len(t1) != len(t2) or len(t1[0]) != len(t2[0]):
        return False  # Retorna False se os tamanhos forem diferentes
    
    # Itera sobre cada linha dos tabuleiros
    for i in range(len(t1)):
        # Compara as linhas correspondentes dos dois tabuleiros
        if t1[i] != t2[i]:
            return False  # Retorna False se alguma linha for diferente
    
    return True  # Retorna True se todos os testes passarem, indicando que os tabuleiros são iguais

def tabuleiro_para_str(tab):
    '''
    função: devolve a cadeia de caracteres que representa o tabuleiro
como mostrado nos exemplos.
    argumentos: tabuleiro'''
    letras = 'abcdefghij'  # Define as letras válidas para as colunas
    # Inicializa a string do tabuleiro com os cabeçalhos das colunas
    tabuleiro_str = "    " + "   ".join(letras[:len(tab[0])]) + "\n"
    
    # Itera sobre cada linha do tabuleiro
    for linha, valor_linha in enumerate(tab):
        # Adiciona o número da linha e os valores das colunas na string do tabuleiro
        tabuleiro_str += f"{linha + 1:02d} " + "".join(f"[{'X' if valor_coluna == 1 else 'O' if valor_coluna == -1 else ' '}]-" for valor_coluna in valor_linha)[:-1]
        
        # Adiciona as linhas divisórias entre as linhas do tabuleiro, exceto na última linha
        if linha != len(tab) - 1:
            tabuleiro_str += "\n    " + "|   " * (len(tab[0]) - 1) + "|\n"
    
    # Retorna a string do tabuleiro formatado
    return tabuleiro_str

def obtem_valor(tab, pos): #função adicional
    '''
    função: devolve o valor na posição p do tabuleiro t.
    argumentos: tabuleiro e posição'''
    # Obtém as coordenadas (linha, coluna) da posição fornecida
    y, g = obtem_coordenadas(pos)
    # Retorna o valor na posição do tabuleiro
    return tab[y][g]

def move_pedra(tab, pos, pos_nova):
    '''
    função: modifica destrutivamente o tabuleiro t movendo a pedra da
posição p1 para a posição p2, e devolve o próprio tabuleiro.
    argumentos: tabuleiro, posição original e posição nova'''
    # Verifica se ambas as posições são válidas
    if not (eh_posicao(pos) and eh_posicao(pos_nova)):
        return tab  # Retorna o tabuleiro inalterado se alguma posição for inválida
    # Verifica se ambas as posições são válidas no contexto do tabuleiro
    if not (eh_posicao_valida(pos, len(tab) // 2) and eh_posicao_valida(pos_nova, len(tab) // 2)):
        return tab  # Retorna o tabuleiro inalterado se alguma posição não for válida no tabuleiro
    # Verifica se a posição original está vazia
    if obtem_valor(tab, pos) == 0:
        return tab  # Retorna o tabuleiro inalterado se a posição original estiver vazia
    # Verifica se a nova posição não está vazia
    if obtem_valor(tab, pos_nova) != 0:
        return tab  # Retorna o tabuleiro inalterado se a nova posição não estiver vazia
    # Obtém a pedra na posição original
    pedra = obtem_pedra(tab, pos)
    # Coloca a pedra na nova posição
    tab = coloca_pedra(tab, pos_nova, pedra)
    # Remove a pedra da posição original
    tab = remove_pedra(tab, pos)
    # Retorna o tabuleiro atualizado
    return tab

def obtem_posicoes_ordenadas_orbitas(n): #função adicional
    '''
    função: devolve um tuplo de tuplos com as posições do tabuleiro de Orbito-n ordenadas por órbitas
    argumentos: quantidade de órbitas do tabuleiro'''
    posicoes = ordena_posicoes_tabuleiro(n)  # Obtém todas as posições ordenadas do tabuleiro
    orbitas = []  # Inicializa uma lista para armazenar as órbitas
    inicio = 0  # Define o índice inicial
    incremento = 4  # Define o incremento inicial
    # Enquanto o índice inicial for menor que o número de posições
    while inicio < len(posicoes):
        fim = inicio + incremento  # Calcula o índice final da órbita atual
        orbitas.append(tuple(posicoes[inicio:fim]))  # Adiciona a órbita atual à lista de órbitas
        inicio = fim  # Atualiza o índice inicial para a próxima órbita
        incremento += 8  # Aumenta o incremento para a próxima órbita

    return tuple(orbitas)  # Retorna as órbitas como um tuplo de tuplos

def obtem_posicao_seguinte(tab, pos, s):
    '''
    função:  devolve a posição da mesma órbita que p que se
encontra a seguir no tabuleiro t em sentido horário se s for True ou anti-horário
se for False
    argumentos: tabuleiro, posição e sentido'''
    # Obtém as órbitas ordenadas do tabuleiro
    orbitas = obtem_posicoes_ordenadas_orbitas(len(tab) // 2)
    # Itera sobre cada órbita
    for orbita in orbitas:
        # Verifica se a posição está na órbita atual
        if pos in orbita:
            # Obtém o índice da posição na órbita
            index = orbita.index(pos)
            # Retorna a próxima posição na órbita se 's' for True, caso contrário, retorna a posição anterior
            if s:
                return orbita[(index + 1) % len(orbita)]
            else:
                return orbita[(index - 1 + len(orbita)) % len(orbita)]

def roda_tabuleiro(tab):
    '''
    função: modifica destrutivamente o tabuleiro t rodando todas as pedras
uma posição em sentido anti-horário, e devolve o próprio tabuleiro.
    argumentos: tabuleiro'''
    # Obtém as órbitas ordenadas do tabuleiro
    orbitas = obtem_posicoes_ordenadas_orbitas(len(tab) // 2)
    # Itera sobre cada órbita
    for orbita in orbitas:
        # Obtém as pedras nas posições da órbita
        valores = [obtem_pedra(tab, pos) for pos in orbita]
        # Itera sobre cada posição na órbita
        for i, pos in enumerate(orbita):
            # Calcula a nova posição para a pedra
            nova_pos = orbita[(i - 1) % len(orbita)]
            # Coloca a pedra na nova posição
            tab = coloca_pedra(tab, nova_pos, valores[i])
    # Retorna o tabuleiro atualizado
    return tab

def obtem_linhas(tab, pos, linhas): #função adicional
    '''
    função: devolve um tuplo de tuplos com as posições das linhas
horizontais ou verticais que passam pela posição p, ordenadas de acordo com a 
ordem de leitura do tabuleiro
    argumentos: tabuleiro, posição e função de linhas'''
    # Verifica se a função de linhas fornecida é obtem_linhas_diagonais
    if linhas == obtem_linhas_diagonais:
        # Obtém as linhas diagonais descendente e ascendente
        linha_dd, linha_da = obtem_linhas_diagonais(tab, pos)
        # Retorna as posições das linhas diagonais
        return tuple(tuple(p for p, _ in linha) for linha in (linha_dd, linha_da))
    # Retorna as posições das linhas horizontais ou verticais
    return tuple(p for p, _ in linhas(tab, pos))

def conta_pedras_consecutivas(tab, linha, jogador): #função adicional
    '''
    função: devolve o número máximo de pedras consecutivas do jogadorna linha fornecida
    argumentos: tabuleiro, linha e pedra do jogador'''
    max_consecutivas = 0  # Inicializa o máximo de pedras consecutivas
    consecutivas = 0  # Inicializa o contador de pedras consecutivas

    # Verifica se a linha é uma linha diagonal (contém tuplos de tuplos)
    if isinstance(linha[0], tuple) and isinstance(linha[0][0], tuple):
        (dd, da) = linha  # Desempacota as diagonais descendente e ascendente

        # Itera sobre cada posição na diagonal descendente
        for pos in dd:
            if obtem_valor(tab, pos) == jogador:  # Verifica se a pedra na posição é do jogador
                consecutivas += 1  # Incrementa o contador de pedras consecutivas
                max_consecutivas = max(max_consecutivas, consecutivas)  # Atualiza o máximo de pedras consecutivas
            else:
                consecutivas = 0  # Reseta o contador se a pedra não for do jogador

        consecutivas = 0  # Reseta o contador para a próxima diagonal

        # Itera sobre cada posição na diagonal ascendente
        for pos in da:
            if obtem_valor(tab, pos) == jogador:  # Verifica se a pedra na posição é do jogador
                consecutivas += 1  # Incrementa o contador de pedras consecutivas
                max_consecutivas = max(max_consecutivas, consecutivas)  # Atualiza o máximo de pedras consecutivas
            else:
                consecutivas = 0  # Reseta o contador se a pedra não for do jogador
    else:
        # Itera sobre cada posição na linha horizontal ou vertical
        for pos in linha:
            if obtem_valor(tab, pos) == jogador:  # Verifica se a pedra na posição é do jogador
                consecutivas += 1  # Incrementa o contador de pedras consecutivas
                max_consecutivas = max(max_consecutivas, consecutivas)  # Atualiza o máximo de pedras consecutivas
            else:
                consecutivas = 0  # Reseta o contador se a pedra não for do jogador

    return max_consecutivas  # Retorna o máximo de pedras consecutivas

def verifica_linha_pedras(tab, posicao, jogador, k):
    '''
    função: devolve True se existe pelo menos uma linha (horizontal, vertical ou diagonal) que contenha a posição p com k ou mais pedras
consecutivas do jogador com pedras j, e False caso contrário.
    argumentos: tabuleiro, posição, pedra do jogador e número mínimo de pedras consecutivas
'''
    # Verifica se a pedra na posição é do jogador
    if jogador == obtem_pedra(tab, posicao):
        # Obtém as linhas diagonais descendente e ascendente
        diagonal_descendente, diagonal_ascendente = obtem_linhas(tab, posicao, obtem_linhas_diagonais)
        # Verifica se há k ou mais pedras consecutivas na linha horizontal
        if conta_pedras_consecutivas(tab, obtem_linhas(tab, posicao, obtem_linha_horizontal), jogador) >= k:
            return True
        # Verifica se há k ou mais pedras consecutivas na linha vertical
        if conta_pedras_consecutivas(tab, obtem_linhas(tab, posicao, obtem_linha_vertical), jogador) >= k:
            return True
        # Verifica se há k ou mais pedras consecutivas na diagonal descendente
        if conta_pedras_consecutivas(tab, diagonal_descendente, jogador) >= k:
            return True
        # Verifica se há k ou mais pedras consecutivas na diagonal ascendente
        if conta_pedras_consecutivas(tab, diagonal_ascendente, jogador) >= k:
            return True
    
    # Retorna False se nenhuma das condições acima for satisfeita
    return False

def eh_vencedor(tab, pedra):
    '''
    função:  é uma função auxiliar que recebe um tabuleiro e uma pedra de jogador,
e devolve True se existe uma linha completa do tabuleiro de pedras do jogador ou False
caso contrário.
    argumentos: tabuleiro e pedra do jogador'''
    # Itera sobre cada posição ordenada do tabuleiro
    for pos in ordena_posicoes_por_leitura(len(tab) // 2):
        # Verifica se há uma linha de pedras consecutivas do jogador na posição atual
        if verifica_linha_pedras(tab, pos, pedra, len(tab)):
            return True  # Retorna True se encontrar uma linha de pedras consecutivas
    return False  # Retorna False se não encontrar nenhuma linha de pedras consecutivas

def eh_fim_jogo(tab):
    '''
    função: é uma função auxiliar que recebe um tabuleiro e devolve True se o jogo
já terminou ou False caso contrário.
    argumentos: tabuleiro'''
    # Verifica se o tabuleiro tem um vencedor com pedras pretas ou brancas ou se todas as posições estão ocupadas
    return eh_vencedor(tab, cria_pedra_preta()) or eh_vencedor(tab, cria_pedra_branca()) or all(type(linha)==list and all(pedra != 0 for pedra in linha) for linha in tab)

def escolhe_movimento_manual(tab):
    '''
    função: é uma função auxiliar que recebe um tabuleiro t e permite
escolher uma posição livre do tabuleiro onde colocar uma pedra. A função não modifica
o seu argumento e devolve a posição escolhida. A função deve apresentar as mensagens
do exemplo a seguir, repetindo as mensagens até o jogador introduzir a representação
externa de uma jogada válida.
    argumentos: tabuleiro'''
    while True:
        # Solicita ao usuário que escolha uma posição livre
        posicao_str = input("Escolha uma posicao livre:")
        
        # Verifica se a string fornecida representa uma posição válida
        if eh_posicao(posicao_str):
            # Converte a string para uma posição (tuplo)
            posicao = str_para_posicao(posicao_str)
            
            # Verifica se a posição é válida no contexto do tabuleiro e se está livre
            if eh_posicao_valida(posicao, len(tab) // 2) and obtem_valor(tab, posicao) == 0:
                # Retorna a posição válida e livre escolhida pelo usuário
                return posicao

def escolhe_movimento_auto(tab, jog, lvl):
    '''
    função: e uma função auxiliar que recebe um tabuleiro t (em
que o jogo não terminou ainda), uma pedra j, e a cadeia de carateres lvl correspondente
à estratégia, e devolve a posição escolhida automaticamente de acordo com a estratégia
selecionada para o jogador com pedras j. A função não modifica nenhum dos seus
argumentos. As estratégias a seguir devem ser as descritas na seção 1.3 e identificadas
pelas cadeias de carateres 'facil' ou 'normal'.
    argumentos: tabuleiro, pedra do jogador e nível de dificuldade'''
    if lvl == 'facil':
        # Verifica se todas as posições do tabuleiro estão vazias
        if all(pedra == 0 for linha in tab for pedra in linha):
            # Retorna a primeira posição ordenada se o tabuleiro estiver vazio
            return ordena_posicoes_por_leitura(len(tab) // 2)[0]
        
        # Cria uma cópia do tabuleiro e roda a cópia
        tab_copia_roda = roda_tabuleiro(cria_copia_tabuleiro(tab))
        
        # Obtém as posições das pedras do jogador
        pedras_jogador = obtem_posicoes_pedra(tab, jog)
        
        # Obtém as posições livres no tabuleiro original e no tabuleiro rodado
        pos_livres = [pos for pos in ordena_posicoes_por_leitura(len(tab) // 2) if obtem_valor(tab, pos) == 0]
        pos_livres_rodado = [pos for pos in ordena_posicoes_por_leitura(len(tab) // 2) if obtem_valor(tab_copia_roda, pos) == 0]
        
        # Se o jogador não tiver pedras no tabuleiro, retorna a primeira posição livre
        if len(pedras_jogador) == 0:
            return pos_livres[0]
        
        # Inicializa um conjunto para armazenar as posições adjacentes finais no tabuleiro rodado
        adjacentes_final_rodado = set()
        
        # Itera sobre as posições das pedras do jogador no tabuleiro rodado
        for i in obtem_posicoes_pedra(tab_copia_roda, jog):
            # Adiciona as posições adjacentes válidas ao conjunto
            adjacentes_final_rodado.update(pos for pos in obtem_posicoes_adjacentes(i, len(tab)//2, True) if pos in pos_livres_rodado)
        
        # Ordena as posições adjacentes finais
        adjacentes_final_rodado_organizado = ordena_posicoes(tuple(adjacentes_final_rodado), len(tab)//2)
        
        # Itera sobre as posições livres no tabuleiro original
        for i in pos_livres:
            # Retorna a posição se a posição seguinte estiver nas posições adjacentes finais organizadas
            if obtem_posicao_seguinte(tab, i, False) in adjacentes_final_rodado_organizado:
                return i
    
    elif lvl == 'normal':
        # Verifica se todas as posições do tabuleiro estão vazias
        if all(all(pedra == 0 for pedra in linha) for linha in tab):
            # Retorna a segunda posição ordenada se o tabuleiro estiver vazio
            return ordena_posicoes_por_leitura(len(tab) // 2)[1]
        
        # Inicializa variáveis para armazenar os comprimentos das linhas de pedras consecutivas
        L_jog = len(tab)
        L_adv = len(tab)
        L_max_adv = 0
        L_max_jog = 0
        
        # Cria cópias do tabuleiro rodadas uma e duas vezes
        tab_copia_roda_1 = roda_tabuleiro(cria_copia_tabuleiro(tab))
        tab_copia_roda_2 = roda_tabuleiro(cria_copia_tabuleiro(tab_copia_roda_1))
        
        # Obtém as posições livres no tabuleiro original e nas cópias rodadas
        obtem_pos_livre_tab = [pos for pos in ordena_posicoes_por_leitura(len(tab) // 2) if obtem_valor(tab, pos) == 0]
        obtem_pos_livres_2 = [pos for pos in ordena_posicoes_por_leitura(len(tab) // 2) if obtem_valor(tab_copia_roda_2, pos) == 0]
        obtem_pos_livres = [pos for pos in ordena_posicoes_por_leitura(len(tab) // 2) if obtem_valor(tab_copia_roda_1, pos) == 0]
        
        # Inicializa variáveis para armazenar as melhores posições para o jogador e o adversário
        pos_jog = None
        pos_adv = None
        
        # Itera sobre as posições livres na primeira cópia rodada
        for pos in obtem_pos_livres:
            # Cria uma cópia do tabuleiro e roda a cópia
            tab_copia = roda_tabuleiro(cria_copia_tabuleiro(tab))
            # Coloca a pedra do jogador na posição
            coloca_pedra(tab_copia, pos, jog)
            # Verifica as linhas de pedras consecutivas do jogador
            for L_jog in range(len(tab), 0, -1):
                if verifica_linha_pedras(tab_copia, pos, jog, L_jog):
                    # Atualiza a melhor posição do jogador se encontrar uma linha maior
                    if L_jog > L_max_jog:
                        L_max_jog = L_jog
                        pos_jog = pos
        
        # Itera sobre as posições livres na segunda cópia rodada
        for pos_2 in obtem_pos_livres_2:
            L_adv = len(tab)
            # Cria uma cópia do tabuleiro rodada duas vezes
            tab_copia_roda_2 = roda_tabuleiro(roda_tabuleiro(cria_copia_tabuleiro(tab)))
            # Coloca a pedra do adversário na posição
            coloca_pedra(tab_copia_roda_2, pos_2, -jog)
            # Verifica as linhas de pedras consecutivas do adversário
            for L_adv in range(len(tab), 0, -1):
                if verifica_linha_pedras(tab_copia_roda_2, pos_2, -jog, L_adv):
                    # Atualiza a melhor posição do adversário se encontrar uma linha maior
                    if L_adv > L_max_adv:
                        L_max_adv = L_adv
                        pos_adv = pos_2
        
        # Se a melhor linha do adversário tiver comprimento 2, retorna a primeira posição livre
        if L_max_adv == 2:
            return obtem_pos_livre_tab[0]
        
        # Retorna a melhor posição do jogador ou a posição seguinte da melhor posição do adversário
        return obtem_posicao_seguinte(tab, pos_jog if L_max_jog >= L_max_adv else obtem_posicao_seguinte(tab, pos_adv, True), True)

def orbito(n, lvl, pedra):
    '''
    função: é a função principal que permite jogar um jogo completo de Orbiton. 
A função recebe o número de órbitas do tabuleiro, uma cadeia de caracteres que
representa o modo de jogo, e a representação externa de uma pedra (preta ou branca),
e devolve um inteiro identificando o jogador vencedor (1 para preto ou -1 para branco),
ou 0 em caso de empate. O jogo começa sempre com o jogador com pedras pretas e se
desenvolve até o fim como descrito na seção 1.2. Os modos de jogo possíveis são:
• 'facil': Jogo de um jogador contra o computador que utiliza a estratégia fácil
(sec. 1.3). O jogador joga com as pedras com representação externa jog. No fim
do jogo a função mostra o resultado obtido pelo jogador: VITÓRIA, DERROTA ou
EMPATE.
• 'normal': Jogo de um jogador contra o computador que utiliza a estratégia normal
(sec. 1.3). O jogador joga com as pedras com representação externa jog. No fim
do jogo a função mostra o resultado obtido pelo jogador: VITÓRIA, DERROTA ou
EMPATE.
• '2jogadores': Jogo de dois jogadores. No fim do jogo a função mostra o resultado
do jogo: VITÓRIA DO JOGADOR 'X', VITÓRIA DO JOGADOR 'O' ou EMPATE.
    argumentos: número de órbitas, modo de jogo e representação externa da pedra'''
    # Verifica se os argumentos fornecidos são válidos
    if n in range(2, 6) and lvl in ('facil', 'normal', '2jogadores') and pedra in ('X', 'O'):
        # Define a pedra do jogador com base no argumento 'pedra'
        pedra_jogador = cria_pedra_preta() if pedra == 'X' else cria_pedra_branca()
        # Cria um tabuleiro vazio de tamanho 'n*2 x n*2'
        tab = cria_tabuleiro_vazio(n)

        # Se o nível for 'facil' ou 'normal'
        if lvl in ('facil', 'normal'):
            print(f"Bem-vindo ao ORBITO-{n}.")
            print(f"Jogo contra o computador ({lvl}).")
            print(f"O jogador joga com '{pedra}'.")
            # Define a pedra atual como preta
            current = cria_pedra_preta()

            # Exibe o tabuleiro inicial
            print(tabuleiro_para_str(tab))
            # Enquanto o jogo não terminar
            while not eh_fim_jogo(tab):
                # Se for o turno do jogador
                if pedras_iguais(pedra_jogador, current):
                    print('Turno do jogador.')
                    # O jogador escolhe uma posição manualmente
                    pos = escolhe_movimento_manual(tab)
                else:
                    print(f'Turno do computador ({lvl}):')
                    # O computador escolhe uma posição automaticamente
                    pos = escolhe_movimento_auto(tab, current, lvl)

                # Coloca a pedra na posição escolhida
                tab = coloca_pedra(tab, pos, current)
                # Roda o tabuleiro
                tab = roda_tabuleiro(tab)
                # Exibe o tabuleiro atualizado
                print(tabuleiro_para_str(tab))

                # Alterna a pedra atual entre preta e branca
                current = cria_pedra_preta() if pedras_iguais(current, cria_pedra_branca()) else cria_pedra_branca()

            # Verifica se o jogador ou o computador venceu
            jogador_vencedor = eh_vencedor(tab, pedra_jogador)
            computador_vencedor = eh_vencedor(tab, cria_pedra_preta() if pedras_iguais(pedra_jogador, cria_pedra_branca()) else cria_pedra_branca())

            # Exibe o resultado do jogo e retorna o vencedor
            if jogador_vencedor and computador_vencedor:
                print("EMPATE")
                return 0
            elif jogador_vencedor:
                print("VITORIA")
                return 1 if pedras_iguais(pedra_jogador, cria_pedra_preta()) else -1
            elif computador_vencedor:
                print("DERROTA")
                return -1 if pedras_iguais(pedra_jogador, cria_pedra_preta()) else 1
            else:
                print("EMPATE")
                return 0

        # Se o nível for '2jogadores'
        elif lvl == "2jogadores":
            print(f"Bem-vindo ao ORBITO-{n}.")
            print("Jogo para dois jogadores.")
            # Define a pedra atual como preta
            current = cria_pedra_preta()
            # Exibe o tabuleiro inicial
            print(tabuleiro_para_str(tab))
            # Enquanto o jogo não terminar
            while not eh_fim_jogo(tab):
                # Exibe o turno do jogador atual
                print(f"Turno do jogador '{'X' if pedras_iguais(current, cria_pedra_preta()) else 'O'}'.")
                # O jogador escolhe uma posição manualmente
                pos = escolhe_movimento_manual(tab)
                # Coloca a pedra na posição escolhida
                tab = coloca_pedra(tab, pos, current)
                # Roda o tabuleiro
                tab = roda_tabuleiro(tab)
                # Exibe o tabuleiro atualizado
                print(tabuleiro_para_str(tab))
                # Alterna a pedra atual entre preta e branca
                current = cria_pedra_preta() if pedras_iguais(current, cria_pedra_branca()) else cria_pedra_branca()

            # Verifica se o jogador 'X' ou 'O' venceu e exibe o resultado
            if eh_vencedor(tab, cria_pedra_preta()):
                print("VITORIA DO JOGADOR 'X'")
                return 1
            elif eh_vencedor(tab, cria_pedra_branca()):
                print("VITORIA DO JOGADOR 'O'")
                return -1
            else:
                print("EMPATE")
                return 0
    else:
        # Levanta um erro se os argumentos forem inválidos
        raise ValueError("orbito: argumentos invalidos")