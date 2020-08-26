from collections import deque
graph = {'S': ['D', 'E', 'P'],
         'A': [],
         'B': ['A'],
         'C': ['A'],
         'D': ['B', 'C', 'E'],
         'E': ['H', 'R'],
         'F': ['C', 'G'],
         'H': ['P', 'Q'],
         'P': ['Q'],
         'Q': [],
         'R': ['F'],
         'G': []}


def bfsSolution(graph, initialState, goalTest):
    frontier = deque(initialState)

    explored = []

    while frontier:
        state = frontier.popleft()
        #if not state in explored: #no colocar los mismos valores
        explored.append(state)

        if state == goalTest:
            return explored

        neighbours = graph[state]
        for neighbour in neighbours:
            if neighbour not in frontier or neighbour not in explored:
                frontier.append(neighbour)

def dfsSolution(graph, initialState, goalTest):

    frontier = [initialState]
    explored = []

    while frontier:
        state = frontier.pop()
        if not state in explored: #no colocar los mismos valores
            explored.append(state)

        if state == goalTest:
            #print(frontier)
            return explored

        neighbours = graph[state]
        for neighbour in neighbours:
            if neighbour not in frontier or neighbour not in explored:
                frontier.append(neighbour)



print(bfsSolution(graph,'S', 'G'))
print(dfsSolution(graph,'S', 'G'))

