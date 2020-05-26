class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return self.data

class BST:
    def __init__(self, nodes = None):
        self.root = None
        if nodes is not None:
            node = Node(data = nodes.pop())
            self.root = node
            for n in nodes:
                self.insert(n)
    
    def __repr__(self):
        if self.root is None:
            print("Empty Tree")

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data,self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            raise ValueError("No Duplicates")

bst = BST()

bst.insert(4)
bst.insert(3)
bst.insert(5)
bst.insert(1)

