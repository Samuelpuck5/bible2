from engine.Data import *

def persMenosCitado(arg: int):
    resposta = menosCitado(arg)
    if(abs(arg) <= 1):
        return f"O personagem menos citado é {resposta}"

    else:
        return f"O {abs(arg)}° personagem menos citado é {resposta}"
    
def persMenosCitados(arg: int):
    if(arg == 0):
        arg = 3

    listaResposta = []
    for i in range(arg):
        listaResposta.append(menosCitado(i+1))

    resposta = ''
    for item in listaResposta:
        if(item != listaResposta[-1]):
            resposta += item +", "
        else:
            resposta += item
    return f"Os personagens menos citados são: {resposta}"

def persMaisCitado(arg: int):
    resposta = maisCitado(arg)
    if(arg < 1):
        return f"O personagem mais citado é {resposta}"

    else:
        return f"O {arg+1}° personagem mais citado é {resposta}"

def menorVersiculo(arg: int):
    resposta = menorVerso(arg)
    if(arg == 0):
        return f"O menor versículo do velho testamento é: {resposta}"
    
    else:
        return f"O {arg+1}° menor verso do velho testamento é: {resposta} "

def maiorVersiculo(arg: int):
    resposta = maiorVerso(arg)
    if(abs(arg) <= 1):
        return f"O maior versículo do velho testamento é: {resposta}"
    
    else:
        return f"O {abs(arg)}° maior verso do velho testamento é: {resposta}"
    
def maiorCapitulo(arg: int):
    resposta = maiorCap(arg)
    if(abs(arg) <= 1):
        return f"o maior capítulo do antigo testamento é: {resposta}"
    
    else:
        return f"O {arg+1}° maior capitulo do antigo testamento é: {resposta}"

def maiorLivro(arg: int):
    resposta = maisCapitulo(arg)
    if(arg < 1):
        return f"O maior livro do velho testamento é {resposta}"
    else:
        return f"O {arg+1}° maior livro do velho testamento é {resposta}"

def menorLivro(arg: int):
    resposta = menosCapitulo(arg)
    if(abs(arg) <= 1):
        return f"O menor livro do velho testamento é {resposta}"
    else:
        return f"O {abs(arg)}° menor livro do velho testamento é {resposta}"
    
def persPorLivro():
    resposta = mediaPersonagensLivro()
    return f"Em média, existem {resposta:.2f} personagens por livro no velho testamento"

def persPorCapitulo():
    resposta = mediaPersonagensCapitulo()
    return f"Em média, existem {resposta:.2f} personagens por capitulo no velho testamento"

def persPorVerso():
    resposta = mediaPersonagensVersiculos()
    return f"Em média, existem {resposta:.2f} personagens por versículo no velho testamento"

def versoPorLivro():
    resposta = mediaVersiculosLivro()
    return f"Em média, existem {resposta:.2f} versículos por livro no velho testamento"

def versoPorCapitulo():
    resposta = mediaVersiculos()
    return f"Em média, existem {resposta:.2f} versículos por Capítulo no velho testamento"

def capituloPorLivro():
    resposta = mediaCapitulos()
    return f"Em média, existem {resposta:.2f} capítulos por Livro no velho testamento"

def quantPersonagens():
    resposta = totalPersonagem()
    return f"Ao todo, a biblia possui {resposta} nomes citados no velho testamento"

def quantVersos():
    resposta = totalVersiculos()
    return f"No total, o velho testamento possui {resposta} versículos"

def quantVersosLivro(arg: str):
    resposta = totalVersiculosLivro(arg)
    return f"{arg} possui {resposta} versículos"


def quantCapitulos():
    resposta = totalCapitulos()
    return f"O velho testamento possui {resposta} capítulos"

def quantCapituloLivro(arg: str):
    resposta = totalCapitulosLivro(arg)
    return f"{arg} possui {resposta} capítulos"

def quantLivros():
    resposta = totalLivros()
    return f"No velho testamento existem {resposta} livros"

def menorLivros(arg: int):
    resposta = menoresLivros(arg)
    Livros = " ".join(resposta)
    return f"Os menores livros do antigo testamento são: {Livros}"

def livro(index: int):
    resposta = textoLivro(index)

    return f"Esta escrito: {resposta}"