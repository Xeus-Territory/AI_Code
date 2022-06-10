class Graph:
    def __init__(self, list_node):
        self.list_node = list_node
        self.heuristic = {}

    def get_neighbors(self, neighbor_loca):
        return self.list_node[neighbor_loca] if neighbor_loca in self.list_node else []

    def set_heuristic(self, neighbor_heuristic, goal_heuristic):
        self.heuristic[neighbor_heuristic] = goal_heuristic

    def get_heuristic(self, neighbor_heuristic):
        return self.heuristic[neighbor_heuristic]

    def a_star_algorithm(self, startState, goalState):
        frontier = [startState]
        explored = []

        # current_state has present distance from startState to currentState
        # default startState is 0
        current_state = {}
        current_state[startState] = 0

        # mapping state containt an mapping of all nodes
        mapping_state = {}
        mapping_state[startState] = startState

        while(len(frontier) > 0):
            state = None

            for i in frontier:
                if state is None or current_state[i] + self.get_heuristic(i) < current_state[state] + self.get_heuristic(state):
                    state = i

            if state is None:
                return False

            for m, weight in self.get_neighbors(state):
                if m not in frontier and m not in explored:
                    frontier.append(m)
                    mapping_state[m] = state
                    current_state[m] = current_state[state] + weight

                else:
                    if current_state[m] > current_state[state] + weight:
                        current_state[m] = current_state[state] + weight
                        mapping_state[m] = state

                        if m in explored:
                            explored.remove(m)
                            frontier.append(m)

            frontier.remove(state)
            explored.append(state)
            if explored[-1] == goalState:
                return explored

        return False


list_node = {
    'S': [('A', 5), ('B', 6), ('C', 5)],
    'A': [('D', 6), ('E', 7)],
    'B': [('F', 3), ('G', 4)],
    'C': [('H', 6), ('K', 4)],
    'D': [('M', 5), ('N', 8)],
    'E': [('I', 8)],
    'F': [('J', 4), ('L', 4)],
    'K': [('Z', 2)],
}

graph = Graph(list_node)

graph.set_heuristic('S', 12)
graph.set_heuristic('A', 7)
graph.set_heuristic('B', 8)
graph.set_heuristic('C', 9)
graph.set_heuristic('D', 6)
graph.set_heuristic('E', 5)
graph.set_heuristic('F', 4)
graph.set_heuristic('G', 10)
graph.set_heuristic('H', 10)
graph.set_heuristic('I', 6)
graph.set_heuristic('J', 0)
graph.set_heuristic('K', 3)
graph.set_heuristic('L', 0)
graph.set_heuristic('M', 9)
graph.set_heuristic('N', 10)
graph.set_heuristic('Z', 8)


result = graph.a_star_algorithm('S', 'L')
if result:

    s = 'explored: '

    for i in result:

        s += i + " "

        print(s)

else:

    print('404 Not Found!')
