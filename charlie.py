def dist(P1,P2):
    return abs(P1[0] - P2[0]) + abs(P1[1] - P2[1])


class Node:
    def __init__(self,n,c):
        self.name = n
        self.c = c
        self.neighbours = list()

    def add_neighbour(self,v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()

class Matrix:
    nodes = {}

    def add_node(self,node):
        if isinstance(node,Node) and node.name not in self.nodes:
            self.nodes[node.name] = node
            return True
        else:
            return False

    def add_edges(self,N,nodes):
        #nodes is an array of neighbours:
        for node in nodes:
            self.nodes[N].add_neighbour(node)
        return True

    def print_matrix(self):
        for key in sorted(list(self.nodes.keys())):
            print(key + self.nodes[key].neighbours)

    def getSteps(self,start,home,food):
        #To get the number of steps to get all the food.
        #start is the starting place of charlie the dog
        #Home is the home of charlie
        queue = [start]; nSteps = 0; paths = []
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if len(food)>0 and node == food[0]:
                food.pop(0)
                paths.append(queue)
                self.getSteps(node,home,food)
            for adj in Matrix.get(node,[]):
                new_path = [queue]
                new_path.append(adj)
                queue.append(new_path)
        for path in paths:
            nSteps += len(path)
        return nSteps
                


M = Matrix()
matrix = [['F','O','O','F'],['O','C','O','O'],['O','O','O','H'],['F','O','O','O']]
NODES = []
for n in range(16):
    for i in range(4):
        for j in range(4):
            a = Node(str(n),matrix[i][j])
            NODES.append(a)
            n += 1
for N in NODES:
    M.add_node(N)

for i in range(16):
    if i in [5,6,9,10]:
        M.add_edges(NODES[i],[NODES[i-1],NODES[i+1],NODES[i-4],NODES[i+4]])
    if i in [4,8]:
        M.add_edges(NODES[i],[NODES[i+4],NODES[i-4],NODES[i+1]])
    if i in [7,11]:
        M.add_edges(NODES[i],[NODES[i+4],NODES[i-4],NODES[i+1]])
    if i in [1,2]:
        M.add_edges(NODES[i],[NODES[i+4],NODES[i-1],NODES[i+1]])
    if i in [13,14]:
        M.add_edges(NODES[i],[NODES[i-4],NODES[i-1],NODES[i+1]])
    if i == 0:
        M.add_edges(NODES[0],[NODES[4],NODES[1]])
    if i == 12:
        M.add_edges(NODES[12],[NODES[8],NODES[13]])
    if i == 3:
        M.add_edges(NODES[3],[NODES[7],NODES[2]])
    if i == 15:
        M.add_edges(NODES[15],[NODES[14],NODES[11]])
Matrix.getSteps(NODE[],NODE[])

    
    
        
