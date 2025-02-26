from engine.Arvore import Classificador
from engine.Data import NOMES

if __name__ == "__main__":
    tree = Classificador()
    while(True):
        init = str(input(">>> "))
        
        if(init == '-e'):
            print(NOMES)
            exit()
        
        if(len(init) > 1):
            tree.start(init)

 