"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
from ArrayList import ArrayList
from ArrayStack import ArrayStack
from ArrayQueue import ArrayQueue


class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList()
            
    def add_edge(self, i : int, j : int):
        self.adj[i].append(j)

    def remove_edge(self, i : int, j : int):
        for k in range(0,len(self.adj[i])):
            if self.adj[i].get(k) == j:
                return self.adj[i].remove(k)
                
    def has_edge(self, i : int, j: int) ->bool:
        for k in self.adj[i]:
            if k==j:
                return True
        return False

    def out_edges(self, i):
        return self.adj[i]

    def in_edges(self, i) -> List:
        out = ArrayList()
        for j in range(0,self.n):
            if self.has_edge(j,i): out.append(j)
        return out
    
    def bfs(self, r : int):
        seen = np.zeros(self.n, np.bool_)
        l = []
        q = ArrayQueue()
        q.add(r)
        seen[r] = True
        while q.size() > 0:
            i = q.remove()
            l.append(i)
            ngh = self.out_edges(i)
            for k in range(0, ngh.size()):
                j = ngh.get(k)
                if seen[j] == False:
                    q.add(j)
                    seen[j] = True
        return l

    def dfs(self, r : int):
        seen = np.zeros(self.n, np.bool_)
        l = []
        s = ArrayStack()
        s.push(r)
        while s.size() > 0:
            i = s.pop()
            l.append(i)
            seen[i] = True
            ngh = self.out_edges2(i)
            for j in range(0, ngh.size()):
                if seen[ngh.get(j)] == False:
                    s.push(ngh.get(j))
                else:
                    continue
        return l
                    
    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s




