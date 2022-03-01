# Name: Jumana Haseen
# StudentID: 2021627 
# Class: DAAA/FT/2B/02

# Import libraries and modules
import networkx as nx
import matplotlib.pyplot as plt
import random

# DrawTree class to draw the parse tree using networkx
class DrawTree:
    def __init__(self, edgeList, fileName):
        self.edges=edgeList
        self.file=fileName

    # Ensure the eexpression can be built into a tree
    def verifyTree(self, G, root=None, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
        '''        
        If the graph is a tree this will return the positions to plot this in a 
        hierarchical layout.
        
        G: the graph (must be a tree)
        
        root: the root node of current branch 
        - if the tree is directed and this is not given, 
        the root will be found and used
        - if the tree is directed and this is given, then 
        the positions will be just for the descendants of this node.
        - if the tree is undirected and not given, 
        then a random choice will be used.
        
        width: horizontal space allocated for this branch - avoids overlap with other branches
        
        vert_gap: gap between levels of hierarchy
        
        vert_loc: vertical location of root
        
        xcenter: horizontal location of root
        '''
        if not nx.is_tree(G):
            raise TypeError('cannot use hierarchy_pos on a graph that is not a tree')

        if root is None:
            if isinstance(G, nx.DiGraph):
                root = next(iter(nx.topological_sort(G)))  #allows back compatibility with nx version 1.11
            else:
                root = random.choice(list(G.nodes))

        getNodePos = self.getPos(G, root, width, vert_gap, vert_loc, xcenter)  
        return getNodePos

    # Get the coordinates of the position of all nodes in tree
    def getPos(self, G, root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos = None, parent = None):
            if pos is None:
                pos = {root:(xcenter,vert_loc)}
            else:
                pos[root] = (xcenter, vert_loc)
            children = list(G.neighbors(root))
            if not isinstance(G, nx.DiGraph) and parent is not None:
                children.remove(parent)  
            if len(children)!=0:
                dx = width/len(children) 
                nextx = xcenter - width/2 - dx/2
                for child in children:
                    nextx += dx
                    pos = self.getPos(G,child, width = 0.5, vert_gap = vert_gap, 
                                        vert_loc = vert_loc-vert_gap, xcenter=nextx,
                                        pos=pos, parent = root)
            return pos

    # Save the image in the file given by user
    def saveTree(self):
        G=nx.Graph()
        G.add_edges_from(self.edges)
        pos = self.verifyTree(G,self.edges[0][0])
        nx.draw(G, pos=pos, with_labels=True, node_size=1000)
        plt.savefig(self.file)


