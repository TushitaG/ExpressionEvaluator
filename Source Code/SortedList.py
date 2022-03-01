# Name: Jumana Haseen
# StudentID: 2021627
# Class: DAAA/FT/2B/02

# Import modules
from Node import Node

# SortedList class to append sorted items
class SortedList:
    # Constructor function
    def __init__(self):
        self.headNode = None
        self.currentNode = None
        self.length = 0

    # Append node to the right of the list
    def __appendToHead(self, newNode):
        oldHeadNode = self.headNode
        self.headNode = newNode
        self.headNode.nextNode = oldHeadNode
        self.length += 1
    
    def insert(self, newNode):
        self.length += 1

        # If list is currently empty
        if self.headNode == None:
            self.headNode = newNode
            return

        # Check if it is going to be new head
        if newNode < self.headNode:
            self.__appendToHead(newNode)
            return

        # Check it is going to be inserted
        # between any pair of Nodes (left, right)
        leftNode = self.headNode
        rightNode = self.headNode.nextNode

        while rightNode != None:
            if newNode < rightNode:
                leftNode.nextNode = newNode
                newNode.nextNode = rightNode
                return
            leftNode = rightNode
            rightNode = rightNode.nextNode

        # Once we reach here it must be added at the tail
        leftNode.nextNode = newNode

    # Returning of each node in str    
    def __str__(self):
        # We start at the head
        output =""
        node= self.headNode
        firstNode = True
        while node != None:
            if firstNode:
                output = node.__str__()
                firstNode = False
            else:
                output += (', ' + node.__str__())
            node= node.nextNode
        return output