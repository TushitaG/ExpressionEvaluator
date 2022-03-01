# Name: Jumana Haseen
# StudentID: 2021627
# Class: DAAA/FT/2B/02

# Import libraries and modules
from VerticalTree import VerticalTree
import numpy as np

# ConstructTree class to construct the expression tree  
class ConstructTree:
    def __init__(self, expList):
        self.expList=expList

    # Get the different depth levels in expression tree
    def getUniqueExpLvl(self):
        separator=VerticalTree('?').getSeparator()
        return list(set([i.count(separator) for i in self.expList]))
    
    # Create dictionary of characters in expression and its depth level
    def treeDict(self):
        tdict=dict()
        expLvl=self.getUniqueExpLvl()
        separator=VerticalTree('?').getSeparator()
        for lvl in expLvl:
            itemNo=0
            for exp in self.expList:
                if exp.count(separator)==lvl:
                    tdict[f'{lvl}-{itemNo}']=exp.replace(separator,'')
                    itemNo=itemNo+1
        return tdict

    # make each character in the expression unique by adding space
    def makeCharUnique(self):
        tdict=self.treeDict()
        for k,v in tdict.items():
            spacing=list(tdict.values()).count(v)
            if list(tdict.values()).count(v)>1:
                tdict[k]=v.center(len(v+' '*(spacing-1)), " ")  
        return tdict

    # sort the elements such that the operator always comes first for different depth levels
    def sortDictElements(self):
        uniqueTdict=self.makeCharUnique()
        for k,v in uniqueTdict.items():
            if (int(k.split("-",1)[1])%2!=0) and (v.replace(' ','') in ['*','+','/','-','**']):
                storage=v
                uniqueTdict[k]=list(uniqueTdict.values())[list(uniqueTdict.values()).index(v)-1]
                nextk=list(uniqueTdict.keys())[list(uniqueTdict.keys()).index(k)-1]
                uniqueTdict[nextk]=storage
        return uniqueTdict

    # Get the indexes of head nodes
    def getHeadNodes(self):
        treeDict=self.sortDictElements()
        headNodeLt=list()
        for i in range(len(list(treeDict.items()))):
            if list(treeDict.items())[i][1].replace(' ','') in ['*','+','/','-','**']:
                headNodeLt.append(i)
        return list(map(list,(np.split(headNodeLt, np.where(np.diff(headNodeLt) != 1)[0]+1))))

    # Get the edge list for the building of the tree
    def getEdgeList(self):
        edgeList=list()
        headNodesLt=self.getHeadNodes()
        treeDict=self.sortDictElements()
        for headNode in headNodesLt:
            for node in headNode:
                if len(headNode)>1 or node==0:
                    edgeList.append((list(treeDict.values())[node], list(treeDict.values())[node+node+1]))
                    edgeList.append((list(treeDict.values())[node], list(treeDict.values())[node+node+2]))
                elif len(headNode)>1:
                    edgeList.append((list(treeDict.values())[node], list(treeDict.values())[node+2]))
                    edgeList.append((list(treeDict.values())[node], list(treeDict.values())[node+3]))            
        return edgeList
