from engine.Engine import *
from random import choice, choices

class Arvore:
    def __init__(self, name = ''):
        self.pontuacao = 0
        self.ord = 0
        self.tex = 0
        self.liv = 0
        self.cap = 0
        self.ver = 0
        self.per = 0
        self.sin = 0
        self.plu = 0
        self.qua = 0
        self.pos = 0
        self.med = 0
        self.neg = 0
        self.num = -1
        self.name = name

    def main(self):
        #menor quantidade
        if(self.neg == 1):
            if(self.sin == 1 and self.plu == 0):
                if(self.per == 1): #personagem menos citado
                   return persMenosCitado(self.num[-1]+1)
                
                elif(self.ver == 1 and self.liv == 0):#menor versiculo
                    return menorVersiculo(self.num[-1])
                
                elif(self.cap == 1 and self.liv == 0):#menor capitulo
                    return menorCap(self.num[-1]+1)

                elif(self.liv == 1):#menor livro
                    return menorLivro(self.num[-1]+1)

            elif(self.plu == 1):
                if(self.per == 1): #personagens menos citados
                    return persMenosCitados(self.num[-1])
                
                elif(self.ver == 1 and self.liv == 0): #menores versiculos
                    pass

                elif(self.cap == 1 and self.liv == 0): #menores capitulos
                    pass

                elif(self.liv == 1): #menores livros
                    return menorLivros(self.num[-1]+1)
    
        #maior quantidade
        elif(self.pos == 1):
            if(self.sin == 1):
                if(self.per == 1): #personagem mais citado
                    return persMaisCitado(self.num[-1])
                
                elif(self.ver == 1 and self.liv == 0): #maior versiculo
                    return maiorVersiculo(self.num[-1]+1)
                
                elif(self.cap == 1 and self.liv == 0): #maior capitulo
                    return maiorCapitulo(self.num[-1]+1)

                elif(self.liv == 1): #maior livro
                    return maiorLivro(self.num[-1])
            elif(self.plu == 1):
                if(self.per == 1): #personagens mais citados
                    pass

                elif(self.ver == 1 and self.liv == 0): #maiores versiculos
                    pass

                elif(self.cap == 1 and self.liv == 0): #maiores capitulos
                    pass

                elif(self.liv == 1): #maiores livros
                    pass
        
            #medias
        elif(self.med == 1):
            if(self.per == 1):
                if(self.liv == 1): #personagens por livro
                    return persPorLivro()

                elif(self.cap == 1): #personagens por capitulo
                    return persPorCapitulo()

                elif(self.ver == 1): #personagen por versiculo
                    return persPorVerso()
                
                else:
                    return persPorLivro()

            elif(self.ver == 1):
                if(self.liv == 1): #versiculo por livro
                    return versoPorLivro()

                elif(self.cap == 1): #versiculo por capitulo
                    return versoPorCapitulo()
                
                else: 
                    return versoPorLivro()

            else: #capitulos por livro
                return capituloPorLivro()

        #quantidades
        elif(self.qua == 1):
        
            if(self.per == 1):
                if(self.liv == 1): #personagens e um livro especifico
                    pass
                
                else: #personagens em toda biblia
                    return quantPersonagens()

            elif(self.ver == 1):
                if(self.liv == 1):
                    if(self.cap == 1): #versiculos em um capitulo especifico
                        pass
                    
                    else: #versiculos em todo livro
                        return quantVersosLivro(self.name)
                
                else: #versiculos em toda biblia
                    return quantVersos()
                
            elif(self.cap == 1):
                if(self.liv == 1): #capitulos em um livro especifico
                    return quantCapituloLivro(self.name)

                else: #capitulos em toda biblia
                    return quantCapitulos()
                
            else: # livros do velho testamento
                return quantLivros()
    
            #textos
        if(self.name != '' and self.tex == 1):
            if(self.cap == 1):
                if(self.ver == 1): #versiculo especifico
                    return Textversiculo(self.name,self.num[-2],self.num[-1])
                
                else: #todo texto de um capitulo
                    return Textcapitulo(self.num[-1],self.name)
            
            elif(self.sin == 1): #todo texto de um livro
                return livro(self.name)

    def mostrarSinal(self):
        print(f"ordem:{self.ord}")
        print(f"texto:{self.tex}")
        print(f"Livro:{self.liv}")
        print(f"Capitulo:{self.cap}")
        print(f"Versiculo:{self.ver}")
        print(f"Personagem:{self.per}")
        print(f"Quant:{self.qua}")
        print(f"QuanPos:{self.pos}")
        print(f"QuanMed:{self.med}")
        print(f"QuanNeg:{self.neg}")
        print(f"Plural:{self.plu}")
        print(f"Singular:{self.sin}")
        print(f"Numero:{self.num}")
        print(f"Escrita: {self.name}")
    

class Classificador:
    def __init__(self):
        self.entrada: str

        #Sinalizadores para auxiliar a classificação dos dados
        self.sinOrdinal = 0 #indica que a busca possui um termo ordinal (primeiro, segundo etc...)
        self.sinTexto = 0 #indica que a busca é para um texto
        self.sinLivro = 0 #indica que a busca é para um livro
        self.sinCapitulo = 0 #indica que a busca é para um capitulo
        self.sinVersiculo = 0 #indica que a busca é para um versiculo
        self.sinPersonagem = 0 #indica que a busca é para um personagem
        self.sinSingular = 0 #indica que a busca é para apenas um elemento
        self.sinQuant = 0 #indica que a busca é para uma quantidade
        self.sinPlural = 0 #indica que a busca é para mais de um elemento
        self.sinQuanPos = 0 #indica que a busca possui um quantificador positivo
        self.sinQuanMed = 0 #indica que a busca possui um qauntificador medio
        self.sinQuanNeg = 0 #indica que a busca possui um quantificador negativo
        self.sinNumero = [0] #sinalizador especial, ele deve ser usado para coletar um numero
        self.sinEscrita = [0,''] #sinaliza que a busca é para um conteudo da biblia

    #funções para definir os pontos da entrada
    def fPronome(self, arg: list):
        pronomes = ('qual','quem')
        pronomesPlural = ('quantos','quantas')
        pontos = 0
        for item in arg:
            if(item in pronomes):
                self.sinSingular = 1 #a busca é para um unico elemento
                if(item == 'quem'): #nota maior para o termo 'quem', indica que é um personagem
                    self.sinPersonagem = 1
                    pontos+= 3
            
                pontos += 1
            
            if(item in pronomesPlural):
                self.sinPlural = 1
                self.sinQuant = 1
                pontos+= 5

        return pontos
    
    def fSubistantivo(self, arg: list):
        substantivos = ('personagem','pessoa','individuo','livro','capitulo','versiculo')
        substantivosPlural = ('personagens','pessoas','individulos','livros','capitulos','versiculos')
        pontos = 0
        for item in arg:
            if(item in substantivos):
                self.sinSingular = 1
                if(item in substantivos[:3]): #indica que a busca é para um personagem
                    self.sinPersonagem = 1
                    pontos += 3
                if(item in substantivos[3:]): #indica que a busca é para um texto
                    self.sinTexto = 1
                
                    match(item):
                        case 'versiculo':self.sinVersiculo = 1
                        case 'capitulo':self.sinCapitulo = 1
                        case 'livro':self.sinLivro = 1

                    pontos += 3
            
            if(item in substantivosPlural):
                self.sinPlural = 1
                if(item in substantivosPlural[:3]): 
                    self.sinPersonagem = 1
                    pontos += 8
            if(item in substantivosPlural[3:]): 
                    self.sinTexto = 1
                    match(item):
                        case 'versiculos':self.sinVersiculo = 1
                        case 'capitulos':self.sinCapitulo = 1
                        case 'livros':self.sinLivro = 1
                        
                    pontos += 8
            
        return pontos
    
    def fQuantificador(self, arg: list):
        quantificadorPositivo = ('mais','maior','maiores')
        quantificadorMedio = ('media','meio')
        quantificadorNegativo = ('menos','menor','menores')
        pontos = 0
        for item in arg:
            if(item in quantificadorPositivo):
                self.sinQuanPos = 1
                pontos += 5
            if(item in quantificadorMedio):
                self.sinQuanMed = 1
                pontos += 3
            if(item in quantificadorNegativo):
                self.sinQuanNeg = 1
                pontos += 1
        return pontos
    
    def fVerbos(self, arg: list):
        verbos = (
            'aparece','apareceu','citado(a)','mencionado(a)','ocorreu',
            'tem','existe','existem','ha','aparecem','possui','escrito')
        pontos = 0
        for item in arg:
            if(item in verbos):
                if(item in verbos[:5]): #indicação de ocorrencia, aparição
                    pontos += 10
                if(item in verbos[5:]): #indicação de existencia, posseção
                    pontos += 20
                    if(item == 'escrito'):
                        self.sinEscrita[0] = 1
        return pontos
    
    def fLivros(self, arg: list):
        livros = [str(nome).lower() for nome in NOMES[:]]
        pontos = 0
        for item in arg:
            if(item in livros):
                self.sinLivro = 1
                pontos += 50
                self.sinEscrita[1] = item
            
        return pontos
    
    def fOrdinal(self, arg: list):
        ordinais = ['primeiro','segundo','terceiro','quarto','quinto','sexto','setimo','oitavo','nono', 'decimo'
                    "11°", "12°", "13°", "14°", "15°", "16°", "17°", "18°", "19°", "20°", "21°", "22°", "23°", 
                    "24°", "25°", "26°", "27°", "28°", "29°", "30°", "31°", "32°", "33°", "34°", "35°", "36°", 
                    "37°", "38°", "39°", "40°", "41°", "42°", "43°", "44°", "45°", "46°", "47°", "48°", "49°", 
                    "50°", "51°", "52°", "53°", "54°", "55°", "56°", "57°", "58°", "59°", "60°", "61°", "62°", 
                    "63°", "64°", "65°", "66°", "67°", "68°", "69°", "70°", "71°", "72°", "73°", "74°", "75°", 
                    "76°", "77°", "78°", "79°", "80°", "81°", "82°", "83°", "84°", "85°", "86°", "87°", "88°", 
                    "89°", "90°", "91°", "92°", "93°", "94°", "95°", "96°", "97°", "98°", "99°"]

        for item in arg:
            if(item in ordinais or str(item).isdigit()):
                self.sinOrdinal = 1
                self.sinSingular = 1

                if(str(item).isdigit()):
                    self.sinNumero.append(int(item)-1) 
                else:
                    self.sinNumero.append(ordinais.index(item)) 
    
    def limparSinal(self):
        self.sinOrdinal = 0
        self.sinTexto = 0
        self.sinLivro = 0
        self.sinCapitulo = 0
        self.sinVersiculo = 0
        self.sinPersonagem = 0
        self.sinQuant = 0
        self.sinQuanPos = 0
        self.sinQuanMed = 0
        self.sinQuanNeg = 0
        self.sinPlural = 0
        self.sinSingular = 0
        self.sinNumero = [0]
        self.sinEscrita = [0,'']


    #não recebe parametros pois usa a entrada global
    def pontuacao(self):
        conteudo = self.entrada.split()

        pronome = self.fPronome(conteudo)
        substantivo = self.fSubistantivo(conteudo)
        quantificador = self.fQuantificador(conteudo)
        verbo = self.fVerbos(conteudo)
        livro = self.fLivros(conteudo)

        self.fOrdinal(conteudo)

        pontos = pronome + substantivo + quantificador + verbo + livro
        return pontos
    
    def iniciarArvore(self, pontos):
        arvore = Arvore(self.sinEscrita[1])
        arvore.pontuacao = pontos
        arvore.ord = self.sinOrdinal
        arvore.per = self.sinPersonagem
        arvore.tex = self.sinTexto
        arvore.cap = self.sinCapitulo
        arvore.liv = self.sinLivro
        arvore.ver = self.sinVersiculo
        arvore.qua = self.sinQuant
        arvore.pos = self.sinQuanPos
        arvore.med = self.sinQuanMed
        arvore.neg = self.sinQuanNeg
        arvore.num = self.sinNumero[:]
        arvore.plu = self.sinPlural
        arvore.sin = self.sinSingular

        print(arvore.main())
        arvore.mostrarSinal()


    def start(self, entrada:str):
        if(entrada[-1] == "?"):
            entrada = entrada[:-1] #remove o '?'
        
        entrada = entrada.lower() #coloca todas as letras em minusculos
        self.entrada = entrada
        
        pontos = self.pontuacao()
        print(pontos)
        
        self.iniciarArvore(pontos)

        self.limparSinal()
