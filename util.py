import heapq
class nodo:

    def __init__(self, letra, sucesores, estado):
        self.letra=letra
        self.sucesores = sucesores
        self.estado = estado
        self.accion=[]




class PriorityQueue:

    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        pair = (priority, item)
        heapq.heappush(self.heap, pair)

    def pop(self):
        (priority, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0