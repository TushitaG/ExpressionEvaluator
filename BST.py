# Name: Tushita Govindaraj
# StudentID: 2012155
# Class: DAAA/FT/2B/02
from BinaryTree import BinaryTree
class BST(BinaryTree):
    def __init__(self,key,
        leftTree = None,
        rightTree = None):
        #print('BST Constructor is executed')
        super().__init__(key,leftTree,rightTree)
    # Insets value in Binary Tree
    def insert(self, key):
        if self.key == key:
            return
        elif self.key < key:
            if self.rightTree is None:
                self.rightTree = BST(key)
            else:
                self.rightTree.insert(key)
        else: # self.key > key
            if self.leftTree is None:
                self.leftTree = BST(key)
            else:
                self.leftTree.insert(key)
    
    #Function which draws the Binary trees using Line in main.py
    def drawtree(self):
        lines, *_ = self._display()
        for line in lines:
            print(line)
    # Function which draws binary tree according to inputs given by User in main.py
    def _display(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # If tree is Empty
        if self.rightTree is None and self.leftTree is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # If only right tree is empty, then take values from left tree and draw the binary tree
        if self.rightTree is None:
            lines, n, p, x = self.leftTree._display()
            s = '%s' % self.key
            u = len(s)
            line1 = (x + 1) * ' ' + (n - x - 1) * '-' + s
            #print(f"first line is{first_line}")
            line2 = x * ' ' + '|' + (n - x - 1 + u) * ' '
             
            shifted_lines = [line + u * ' ' for line in lines]
            return [line1, line2] + shifted_lines, n + u, p + 2, n + u // 2

        # If only left Tree is empty then take value of nodes in right tree to draw the binary tree
        if self.leftTree is None:
            lines, n, p, x = self.rightTree._display()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '-' + (n - x) * ' '
            second_line = (u + x) * ' ' + '|' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        else:
            # If both children have values combine the codes from above to draw the whole binary tree which consists of values from left and right Tree
            leftTree, n, p, x = self.leftTree._display()
            rightTree, m, q, y = self.rightTree._display()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '-' + s + y * '-' + (m - y) * ' '
            second_line = x * ' ' + '|' + (n - x - 1 + u + y) * ' ' + '|' + (m - y - 1) * ' '
            if p < q:
                leftTree += [n * ' '] * (q - p)
            elif q < p:
                rightTree += [m * ' '] * (p - q)
            zipped_tree = zip(leftTree, rightTree)
                    
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_tree]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
