class Vertices:
    def __init__(self, no) -> None:
        self.no = no
        self.grau = 1
        self.prox = []
        self.an = []
    
    def adicionar_aresta(self, n, x = True):
        self.prox.append(n)
        self.grau += 1
        if x:
            n.adicionar_aresta(self, False)

class Grafo:
    def __init__(self, n) -> None:
        self.numVertices = n
        self.vertices = []
        self.grau = 0
    def addVertice(self, v):
        self.vertices.append(v)
        self.grau += v.grau
        
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
vertice_1 = Vertices(1)
vertice_2 = Vertices(2)
vertice_3 = Vertices(3)
vertice_4 = Vertices(4)
vertice_1.adicionar_aresta(vertice_2)
vertice_2.adicionar_aresta(vertice_3)
vertice_1.adicionar_aresta(vertice_4)
G.addVertice(vertice_1)
G.addVertice(vertice_2)
G.addVertice(vertice_3)
G.addVertice(vertice_4)

for i in G.vertices:
    for j in i.prox:
        print(f"({i.no},{j.no})")
print(G.grau)

for i in G.vertices:
    print(i.grau)

print("@")

G.centroArvore()
for i in G.vertices:
    print(i.no)

print("@")

for i in G.vertices:
    print(i.grau)
print(G.grau)