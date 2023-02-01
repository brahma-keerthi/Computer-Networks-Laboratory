class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printAns(self, dis):
        print("Vertex\t\tDistance from Source >> ")

        for i in range(self.V):
            print(f'{i}\t\t\t{dis[i]}')

    def bellmanFord(self, src):
        dis = [float('Inf')] * self.V
        dis[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dis[v] > w + dis[u] :
                    dis[v] = w + dis[u]

        self.printAns(dis)

def main():
    g = Graph(5)
    # Graph must not contain negative weight cycle
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)
 
    g.bellmanFord(0)

if __name__ == '__main__':
    main()