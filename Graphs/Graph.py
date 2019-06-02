""" Code example from Complexity and Computation, a book about
exploring complexity science with Python.  Available free from

http://greenteapress.com/complexity

Copyright 2011 Allen B. Downey.
Distributed under the GNU General Public License at gnu.org/licenses/gpl.html.

Extended by mossa, april 2017
"""
#import Queue
#import time

class node_object(object):
    __slots__ = ['order', 'vertex', 'edges']
    
class Vertex(object):
    """A Vertex is a node in a graph."""

    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        """Returns a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Vertex(%s)' % repr(self.label)

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Edge(tuple):
    """An Edge is a list of two vertices."""

    def __new__(cls, *vs):
        """The Edge constructor takes two vertices."""
        if len(vs) != 2:
            """raise ValueError, 'Edges must connect exactly two vertices.'"""
            raise 'Edges must connect exactly two vertices.'
        return tuple.__new__(cls, vs)

    def __repr__(self):
        """Return a string representation of this object that can
        be evaluated as a Python expression."""
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__
    """The str and repr forms of this object are the same."""


class Graph(dict):
    """A Graph is a dictionary of dictionaries.  The outer
    dictionary maps from a vertex to an inner dictionary.
    The inner dictionary maps from other vertices to edges.
    
    For vertices a and b, graph[a][b] maps
    to the edge that connects a->b, if it exists."""

    def __init__(self, vs=[], es=[]):
        """Creates a new graph.  
        vs: list of vertices;
        es: list of edges.
        """
        for v in vs:
            self.add_vertex(v)
            
        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        """Add a vertex to the graph."""
        self[v] = {}

    def add_edge(self, e):
        """Adds and edge to the graph by adding an entry in both directions.

        If there is already an edge connecting these Vertices, the
        new edge replaces it.
        """
        v, w = e
        self[v][w] = e
        self[w][v] = e
        
    """3. Write a metod named get_edge that takes two vertices and returns
       the edge between them if it exists and None otherwise"""    
    def get_edge(self, v, w):
        try:
            return self[v][w]
        except:
            return None

    """4. Write a method name remove_edge that takes and edge and removes
       all references to it from the graph"""
    def remove_edge(self, e):
        #print dict.__repr__(self)
        for k,v in self.items():
            try:
                for i in v.values():
                    if i == e:
                        self[k] = []
            except:
                continue
        return
    
    """5. Write a method named vertices that returns a list
       of the vertices in a graph OK"""
    def vertices(self):
        my_list = []
        for vertex,edge in self.items():
            my_list.append(vertex)
        return my_list
    
    """6. Write a method named edges that return a list
       of edges in a graph OK"""
    def edges(self):
        my_list = []
        for vertex,edge in self.items():
            for w in edge.values():
                if not w in my_list:
                    my_list.append(w)
        return my_list
    
    """7. Write a method name out_vertices that takes a Vertex
       and returns a list of the adjacent vertices
       (the ones connected to the given node by an edge)"""
    def out_vertices(self, v):
        adjacent_vertices = []
        for edge in self.edges():
            if v in edge:
                for x in edge:
                    if v != x:
                        if x not in adjacent_vertices:
                            adjacent_vertices.append(x)
        return adjacent_vertices
    
    """8. Write a method named out_edges that takes a Vertex
       and returns a list of edges connected to the given Vertex"""
    def out_edges(self, v):
        edges_connected = []
        for edge in self.edges():
            if v in edge:
                edges_connected.append(edge)
        return edges_connected
    
    """9. Write a method named add_all_edges that starts
       with an edgeless Graph and makes a complete graph
       by adding edges between all pairs of vertices"""
    def add_all_edges(self):
        for v1 in self.vertices():
            for v2 in self.vertices():
                if v1 != v2:
                    self.create_edge(v1, v2)
        return

    """Exercise 2-3. Write a method named add_regular_edges that
       starts with an edgeless graph and adds edges so that every
       vertex has the same degree. The degree of a node is the number
       of edges it is connected to"""
    
    def create_edge(self, v1, v2):
        
        edge = Edge(v1, v2)
        v1, v2 = edge
        self[v1][v2] = edge
        self[v2][v1] = edge
        
        return
    
    def goal_reached(self, k):
        for vertex in self.vertices():
            if len(self.out_edges(vertex)) != k:
                return False
        return True
    
    def find_minor(self, order, k, vertex):
        while order < k:
            for v in self.vertices():
                if v != vertex and len(self.out_edges(v)) == order:
                    if self.out_edges(v) == []:
                        return v
                    found = False
                    for edge in self.out_edges(v):
                        for vertex_tmp in edge:
                            if vertex_tmp == vertex:
                                found = True
                    if not found:
                        return v
            order += 1
        return None
    
    def add_regular_edges(self, k):
        #calculate the number of vertices
        n = len(self.items())
        #figure out if it is possible to build a k-regular graph with this k in particular
        if not ((k > -1 and k < 2 and n > 0 or k == 2 and n > 2) or k > 2 and n >= k+1 and (k*n) % 2 == 0):
            return False
        if n == k+1:
            self.add_all_edges()
            return True

        order = 0
        v1 = self.find_minor(order, k, None)
        while order < k:
            v2 = self.find_minor(order, k, v1)
            if v2 != None:
                n1 = len(self.out_edges(v1))
                n2 = len(self.out_edges(v2))
                if n1 == n2 and n1 != order:
                    order += 1
                self.create_edge(v1, v2)
                v1 = self.find_minor(order, k, None)
            if v1 == None or v2 == None:
                order += 1
                
        if self.goal_reached(k):
            return True
        else:
            return False
    
def main(script, *args):
    v1 = Vertex('v1')
    print (v1)
    v2 = Vertex('v2')
    print (v2)
    v3 = Vertex('v3')
    print (v3)
    v4 = Vertex('v4')
    print (v4)
    v5 = Vertex('v5')
    print (v5)
    v6 = Vertex('v6')
    print (v6)
    e1 = Edge(v1, v2)
    print ("edges: " + str(e1))
    e2 = Edge(v1, v3)
    print ("edges: " + str(e2))
    e3 = Edge(v2, v4)
    print ("edges: " + str(e3))
    g = Graph([v1,v2,v3,v4], [e1,e2,e3])
    print ("graph: " + str(g))
    print ("*" * 10, "edges:")
    print (g.edges())
    print ("*" * 10, "vertices:")
    print (g.vertices())
    print ("*" * 10, "out_vertices for '" + str(v2) + "':")
    print (g.out_vertices(v2))
    print ("*" * 10, "out_edges for '" + str(v2) + "':")
    print (g.out_edges(v2))
    """
    g = Graph([v1,v2,v3,v4,v5,v6], [])
    print "*" * 10, "vertices:"
    print g.vertices()
    print "*" * 10, "edges:"
    print g.edges()
    
    print "*" * 10, "add_all_edges:"
    g.add_all_edges()
    print "edges: " + str(g.edges())
    print "graph: " + str(g)
    
    g = Graph([v1,v2,v3,v4, v5, v6], [])
    print g.add_regular_edges(4)
    print "graph: " + str(g)
    """

if __name__ == '__main__':
    import sys
    main(*sys.argv)
    