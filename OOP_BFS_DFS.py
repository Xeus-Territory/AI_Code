class node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
    def add_neighbor(self, neighbors):
        for neighbor in neighbors:
            self.neighbors.append(neighbor)
    def remove_neighbor(self ,neighbors):
        index = []
        for neighbor in neighbors:
            temp = self.neighbors.index(neighbor)
            index.append(temp)
        for i in range(0, len(index)):
            self.neighbors.pop(index[i])
    def get_node(self):
        print("Node name is: ", self.name)
        print("Node neighbors is: ")
        for neighbor in self.neighbors:
            print(neighbor.name)
    def set_neighbors(self, name, neighbors):
        if (name == ""):
            self.neighbors = neighbors
        else:
            self.name = name
            self.neighbors = neighbors
    
def DFS(inputState, goalState):
    frontier = [inputState]
    explorer = []
    while frontier:
        state = frontier.pop((len(frontier)-1))
        explorer.append(state)
        if goalState == state:
            return explorer
        for neighbor in state.neighbors:
            if neighbor not in (explorer and frontier):
                frontier.append(neighbor)
    return False        

def BFS(inputState, goalState):
    frontier = [inputState]
    explorer = [] 
    while frontier:
        state = frontier.pop(0)
        explorer.append(state)
        if goalState == state:
            return explorer
        for neighbor in state.neighbors:
            if neighbor not in (explorer and frontier):
                frontier.append(neighbor)
    return False

nodeA = node("A")
nodeB = node("B")
nodeC = node("C")
nodeD = node("D")
nodeE = node("E")
nodeF = node("F")
nodeG = node("G")
nodeH = node("H")
nodeI = node("I")  
nodeJ = node("J")
nodeK = node("K")
nodeL = node("L")
nodeM = node("M")
nodeN = node("N")
nodeO = node("O")
nodeA.add_neighbor([nodeB, nodeC])
nodeB.add_neighbor([nodeD, nodeE])
nodeC.add_neighbor([nodeF, nodeG])
nodeD.add_neighbor([nodeH, nodeI])
nodeE.add_neighbor([nodeJ, nodeK])
nodeF.add_neighbor([nodeL, nodeM])
nodeG.add_neighbor([nodeN, nodeO])

print("Result of BFS: ")
result = BFS(nodeA , nodeO)
if result:
    s = 'explored '
    for i in result:
        s  += i.name + ' '
        print(s)
else: 
    print('Error')
    
print ("\n")

print("Result of DFS: ")
result = DFS(nodeA , nodeH)
if result:
    s = 'explored '
    for i in result:
        s  += i.name + ' '
        print(s)
else: 
    print('Error')
  
    