import heapq

class Tree:
    def __init__(self, name, cost = 100000):
        self.name = name
        self.cost = cost
        self.neighbors = []
    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)
    def get_neighbors(self):
        return self.neighbors
    def get_cost(self):
        return self.cost
    def __lt__(self, other):
        return self.cost < other.cost

def update_frontier(frontier, new_node):
    for idx, n in enumerate(array_of_node):
        if n == new_node:
            if frontier[idx].cost > new_node.cost:
                frontier[idx] = new_node

def GBF_search(startState, goalState):
    frontier = []
    explored = []
    heapq.heapify(frontier)
    heapq.heappush(frontier, startState)
    while len(frontier) > 0: 
        state = heapq.heappop(frontier)
        explored.append(state)
        if state == goalState:
            return explored
        for neighbor in state.get_neighbors():
            if neighbor not in (frontier and explored):
                heapq.heappush(frontier, neighbor)
            elif neighbor in frontier:
                update_frontier(frontier=frontier, new_node=neighbor)
    return False

nodeA = Tree("A", 6)
nodeB = Tree("B", 3)
nodeC = Tree("C", 4)
nodeD = Tree("D", 5)
nodeE = Tree("E", 3)
nodeF = Tree("F", 1)
nodeG = Tree("G", 6)
nodeH = Tree("H", 2)
nodeI = Tree("I", 5)  
nodeJ = Tree("J", 4)
nodeK = Tree("K", 2)
nodeL = Tree("L", 0)
nodeM = Tree("M", 4)
nodeN = Tree("N", 0)
nodeO = Tree("O", 4)
nodeA.add_neighbor(nodeB)
nodeA.add_neighbor(nodeC)
nodeA.add_neighbor(nodeD)
nodeB.add_neighbor(nodeE)
nodeB.add_neighbor(nodeF)
nodeC.add_neighbor(nodeG)
nodeC.add_neighbor(nodeH)
nodeD.add_neighbor(nodeI)
nodeD.add_neighbor(nodeJ)
nodeF.add_neighbor(nodeK)
nodeF.add_neighbor(nodeL)
nodeF.add_neighbor(nodeM)
nodeH.add_neighbor(nodeN)
nodeH.add_neighbor(nodeO)

array_of_node = []
array_of_node.append(nodeA)
array_of_node.append(nodeB)
array_of_node.append(nodeC)
array_of_node.append(nodeD)
array_of_node.append(nodeE)
array_of_node.append(nodeF)
array_of_node.append(nodeG)
array_of_node.append(nodeH)
array_of_node.append(nodeI)
array_of_node.append(nodeJ)
array_of_node.append(nodeK)
array_of_node.append(nodeL)
array_of_node.append(nodeM)
array_of_node.append(nodeN)
array_of_node.append(nodeO)

result = GBF_search(nodeA, nodeN)
if result:
    s = 'explored '
    for i in result:
        s  += i.name + ' '
        print(s)
else: 
    print('Error')   