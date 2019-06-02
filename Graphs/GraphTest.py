import string

from Graph import Vertex
from Graph import Edge
from Graph import Graph
from GraphWorld import CircleLayout
from GraphWorld import RandomLayout
from GraphWorld import GraphWorld

try:
    from Gui import Gui, GuiCanvas
except ImportError:
    from swampy.Gui import Gui, GuiCanvas


def main(script, n='10', *args):
    n = int(n)
    labels = string.ascii_lowercase + string.ascii_uppercase
    vs = [Vertex(c) for c in labels[:n]]
    g = Graph(vs)

    if g.add_regular_edges(n-2) == True:
        print (g.edges())
    else:
        print ("I couldn't!")
        for v in g.vertices():
            print (len(g.out_edges(v)))
    # draw the graph
    layout = CircleLayout(g)
    gw = GraphWorld()
    gw.show_graph(g, layout)
    gw.mainloop()


if __name__ == '__main__':
    import sys
    main(*sys.argv)
