def DFS(inputState, goalState):
    frontier = [inputState]
    explorer = []
    while frontier:
        state = frontier.pop((len(frontier)-1))
        explorer.append(state)
        if goalState == state:
            return explorer
        for neighbor in graph[state]:
            if neighbor not in (explorer and frontier):
                frontier.append(neighbor)
    return False


graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : ['H','I'],
    'E' : ['J','K'],
    'F' : ['L','M'],
    'G' : ['N','O'],
    'H' : [],
    'I' : [],
    'J' : [],
    'K' : [],
    'L' : [],
    'M' : [],
    'N' : [],
    'O' : [],
}

result = DFS('A', 'H')
if result:
    s = 'explored '
    for i in result:
        s  += i + ' '
        print(s)
else: 
    print('Error')