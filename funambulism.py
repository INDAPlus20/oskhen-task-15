#!/usr/bin/env python3

#### AVL tree

class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1
        self.balance = 0

    def __repr__(self):
        if self.value == None:
            return f"{self.key}; {self.balance}"
        return f"({self.key}:{self.value})"

    def getHeight(self, node):
        if node == None:
            return 0
        return node.height
    
    def getBalance(self):
        return self.getHeight(self.left) - self.getHeight(self.right)
    
    def setHeight(self):
        return max( self.getHeight(self.left),  self.getHeight(self.right) ) + 1


        
    
    # Prints are stolen from stackoverflow
    def print_tree_values(root, value="value", left="left", right="right"):
        def display(root, value="value", left="left", right="right"):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, value)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, value)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, value)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, value)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, value, left, right) 
        for line in lines:
            print(line)

    def print_tree_keys(root, key="key", left="left", right="right"):
        def display(root, key="key", left="left", right="right"):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, key)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, key)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, key)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, key)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, key, left, right) 
        for line in lines:
            print(line)

class AVL(object):

    def __init__(self):
        self.root = None

    def print_tree(self, value=False):
        if self.root == None:
            print("Tree is empty!")
        elif value == True:
            self.root.print_tree_values()      
        else:
            self.root.print_tree_keys()

    def insert(self, key, value=None, current=None, ret=False):

        newNode = Node(key, value)
        localRoot = None

        if current == None:
            current = self.root

        if self.root == None:
            self.root = newNode

        if current == None:
            current = self.root
        elif key < current.key:
            if current.left == None:
                current.left = newNode
            else:
                localRoot = self.insert(key, value, current.left, True)
                current.left = localRoot
        else: # key => current.key
            if current.right == None:
                current.right = newNode
            else:
                localRoot = self.insert(key, value, current.right, True)
                current.right = localRoot
        
        current.height = current.setHeight()
        current.balance = current.getBalance()

        if current.balance > 1:
            if key < current.left.key:
                current = self.RightRotate(current)
            else:
                current.left = self.LeftRotate(current.left)
                current = self.RightRotate(current)
        elif current.balance < -1:
            if key > current.right.key:
                current = self.LeftRotate(current)
            else:
                current.right = self.RightRotate(current.right)
                current = self.LeftRotate(current)

        if ret:
            return current
        else:
            self.root = current
    
    def search(self, key, current=None, stack=list()):

        if current == None:
            current = self.root

        if key == current.key:
            stack.append(current)

            if current.right == None:
                return stack
            
            self.search(key, current.right, stack)

        if stack:
            return stack

        elif key < current.key:
            if current.left == None:
                return stack

            self.search(key, current.left, stack)

        elif key > current.key:
            if current.left == None:
                return stack
            self.search(key, current.left, stack)
    
    def traverse(self):

        def internal_traversal(current):
            
            if current == None:
                return
            
            stack.append(current)

            internal_traversal(current.left)
            internal_traversal(current.right)

        stack = list()
        current = self.root
        
        internal_traversal(current)
    
        return stack

    def LeftRotate(self, Z):

        Y = Z.right
        T2 = Y.left

        Y.left = Z
        Z.right = T2

        Z.height = Z.setHeight()
        Y.height = Y.setHeight()

        return Y
    
    def RightRotate(self, Z):

        Y = Z.left
        T2 = Y.right

        Y.right = Z
        Z.left = T2

        Z.height = Z.setHeight()
        Y.height = Y.setHeight()

        return Y


tree = AVL()

# Insertion test
tree.insert(13, "I")
tree.insert(15, "To")
tree.insert(10, "AVL")
tree.insert(16, "Trees")
tree.insert(11, "!")
tree.insert(5, "Build")
tree.insert(4, "In")
tree.insert(6, "Like")
print("Tree of keys:")
tree.print_tree()
print("Corresponding values:")
tree.print_tree(True)
tree.insert(7, "Python")
print("-------------After insertion and rebalancing-------------")
print("Tree of keys:")
tree.print_tree()
print("Corresponding values:")
tree.print_tree(True)