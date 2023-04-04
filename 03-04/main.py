class Vertices:
    def __init__(self, no, G, grau) -> None:
        self.no = no
        self.grau = grau + 1
        self.prox = []
        G.addVertice(self)

    def adicionar_arestav(self, n):
        self.prox.append(n)         

class Grafo:
    def __init__(self) -> None:
        self.vertices = []
        self.grau = 0

    def addVertice(self, v):
        self.vertices.append(v)
        self.grau += v.grau

    def adicionar_aresta(self, n, m):
        self.vertices[n-1].adicionar_arestav(self.vertices[m-1])
        self.vertices[m-1].adicionar_arestav(self.vertices[n-1])

    def exibir_arestas(self):
        for i in self.vertices:
            for j in i.prox:
                print(f'({i.no},{j.no})')
        print("\n")

    def removerArvore(self):
        self.list_remov = []
        for i in self.vertices:
            if i.grau == 0:
                self.list_remov.append(i)
        #repetição usada para exibir os vertices que estão sendo removidos
        # for i in self.list_remov:
        #     print(f'--{i.no}')
        for i in self.list_remov:
            self.vertices.remove(i)
        self.list_remov = None

    def centroArvore(self):
        if self.grau > 2:
            for i in self.vertices:
                if i.grau == 2:
                    i.grau -=2
                    self.grau -=2
            for i in self.vertices:
                if i.grau <= 0:
                    for j in i.prox:
                        j.grau -= 1
                        self.grau -=1
            for i in self.vertices:
                list_removprox = []
                for j in i.prox:
                    if j.grau == 0:
                        list_removprox.append(j)
                for j in list_removprox:
                    i.prox.remove(j)
                list_removprox = None
        if self.grau > 2:
            self.removerArvore()  
            self.centroArvore()
        self.removerArvore()

    def Centro(self):
        self.centroArvore()
        print("centro: ")
        for i in G.vertices:
            print(f'{i.no}')
                


G = Grafo()
v = []
'''
grafo 1 centro
'''
v.append(Vertices(1, G, 2))
v.append(Vertices(2, G, 2))
v.append(Vertices(3, G, 2))
v.append(Vertices(4, G, 2))
v.append(Vertices(5, G, 3))
v.append(Vertices(6, G, 1))
v.append(Vertices(7, G, 1))
v.append(Vertices(8, G, 1))
v.append(Vertices(9, G, 2))
v.append(Vertices(10, G, 2))
G.adicionar_aresta(1, 2)
G.adicionar_aresta(1, 10)
G.adicionar_aresta(2, 3)
G.adicionar_aresta(3, 4)
G.adicionar_aresta(4, 5)
G.adicionar_aresta(5, 6)
G.adicionar_aresta(5, 7)
G.adicionar_aresta(8, 9)
G.adicionar_aresta(9, 10)
'''
grafo 2 centros
'''
# v.append(Vertices(1, G, 2))
# v.append(Vertices(2, G, 2))
# v.append(Vertices(3, G, 1))
# v.append(Vertices(4, G, 1))
# G.adicionar_aresta(1, 2)
# G.adicionar_aresta(2, 3)
# G.adicionar_aresta(1, 4)


G.exibir_arestas()
G.Centro()