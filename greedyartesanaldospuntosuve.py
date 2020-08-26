from collections import deque

import util

# graph = {'S': ['A', 'B'],
#          'A': ['F', 'C', 'D'],
#          'B': ['C'],
#          'C': ['A', 'G', 'E'],
#          'D': ['F', 'G'],
#          'E': [],
#          'F': ['D'],
#          'G': []}
# Dir ={'S': [2, 2],
#       'A': [7, 3],
#       'B': [4, 6],
#       'C': [7, 9],
#       'D': [10, 9],
#       'E': [2, 13],
#       'F': [11, 4],
#       'G': [8, 13]}

graph = {'Chepen': ['Pacasmayo', 'Ascope'],
         'Pacasmayo': ['Ascope'],
         'Ascope': ['Chimu', 'Otuzco', 'Trujillo'],
         'Trujillo': ['Julcan', 'Viru'],
         'Viru': ['Julcan', 'Chuco'],
         'Chimu': ['Otuzco','Carrion'],
         'Otuzco': ['Carrion', 'Chuco'],
         'Julcan': ['Viru', 'Chuco'],
         'Chuco':['Carrion'],
         'Carrion':['Bolivar', 'Pataz' ],
         'Bolivar':['Pataz'],
         'Pataz':[]}
Dir = {'Chepen': [2, 3],
         'Pacasmayo': [6, 3],
         'Ascope': [8, 5],
         'Trujillo': [11, 7],
         'Viru': [14, 11],
         'Chimu': [7, 9],
         'Otuzco': [9, 11],
         'Julcan': [12, 11],
         'Chuco':[13, 13],
         'Carrion':[9, 15 ],
         'Bolivar':[6, 17],
         'Pataz':[12, 22]}


def nullHeuristic(Dir,state, goalTest):
    xy1= Dir[state]
    xy2 = Dir[goalTest]

    return abs(xy1[0]-xy2[0])+abs(xy1[1]-xy2[1])

def greedyFirstSearch(graph,Dir, initialState, goalTest, heuristic=nullHeuristic):
  frontier = util.PriorityQueue()
  frontier.push(initialState, 0)
  explorados = []
  while True:
    if frontier.isEmpty():
      return False
    estado = frontier.pop()
    if estado == goalTest:
      explorados.append(estado)
      return explorados
    if estado not in explorados:
      explorados.append(estado)
      sucesores = graph[estado]
      for sucesor in sucesores:
        costo_x = heuristic(Dir, sucesor, goalTest)
        nodo_final = (sucesor)
        frontier.push(nodo_final, costo_x)

print(greedyFirstSearch(graph,Dir,'Chepen', 'Pataz'))

