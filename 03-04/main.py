class Vertices:
    def __init__(self, no, G) -> None:
        self.no = no
        self.grau = 1
        self.prox = []
        G.addVertice(self)
    
    def adicionar_arestav(self, n):
        self.prox.append(n)

class Grafo:
    def __init__(self, n) -> None:
        self.numVertices = n
        self.vertices = []
        self.grau = 0
    def addVertice(self, v):
        self.vertices.append(v)
        self.grau += v.grau
    
    def adicionar_aresta(self, n, m):
        self.vertices[n-1].adicionar_arestav(self.vertices[m-1])
        self.vertices[n-1].grau += 1
        self.vertices[m-1].grau += 1
        self.grau += 2

        
    def removerArvore(self):
        for i in self.vertices:
            if i.grau == 0:
                self.vertices.remove(i)
                self.removerArvore()
    def centroArvore(self):
        if self.grau > 2:
            for i in self.vertices:
                i.grau -= 1
                self.grau -= 1
        self.removerArvore()
        if self.grau > 2:
            self.centroArvore()
        
            
                
G = Grafo(4)
v = []
v.append(Vertices(1, G))
v.append(Vertices(2, G))
v.append(Vertices(3, G))
v.append(Vertices(4, G))
G.adicionar_aresta(1, 2)
G.adicionar_aresta(2, 3)
G.adicionar_aresta(1, 4)


for i in G.vertices:
    for j in i.prox:
        print(f'({i.no},{j.no})')

G.centroArvore()

print("centro: ")
for i in G.vertices:
    print(i.no)