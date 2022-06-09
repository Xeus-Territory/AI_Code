def BFS(inputState, goalState):
    frontier = [inputState]
    explorer = [] 
    while frontier:
        state = frontier.pop(0)
        explorer.append(state)
        if goalState == state:
            return explorer
        for neighbor in graph[state]:
            if neighbor not in (explorer and frontier):
                frontier.append(neighbor)
    return False

def add_node_intree():
    node_parent = input("Input the node_parent into the tree: ")
    node_child = input("Input the node_child into the the tree: ")
    if node_parent in graph.keys():
        print("Cannot set name same with the node in tree")
    else:
        graph[node_parent] = list(node_child)
        
def find_node_intree(node_name_find):
    if node_name_find in graph.keys():
            print("Node name is: ", node_name_find)
            print("Node children are: ", graph[node_name_find])
            
def remove_node_intree(node_name_remove, error_message = "Not found the node_name_remove"):
    graph.pop(node_name_remove, error_message)

def update_node_intree(node_name):
    if node_name in graph.keys():
        node_child_update = input("Input the node_child_update into the the tree: ")
        graph[node_name] = list(node_child_update)  

graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F','G'],
    'D' : ['H','I'],
    'E' : ['J','K'],
    'F' : ['L','M'],
    'G' : ['N','O'],
    'H' : [''],
    'I' : [''],
    'J' : [''],
    'K' : [''],
    'L' : [''],
    'M' : [''],
    'N' : [''],
    'O' : [''],
}

add_node_intree()
update_node_intree('A')
remove_node_intree('B')
find_node_intree('C')
print(graph)
result = BFS('A', 'O')
if result:
    s = 'explored '
    for i in result:
        s  += i + ' '
        print(s)
else: 
    print('Error')

        