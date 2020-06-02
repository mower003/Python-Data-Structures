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
    
    def print_tree(self, traversal_type):
        if traversal_type.lower() == "inorder":
            self.print_inorder(self.root)
            print()
        elif traversal_type.lower() == "postorder":
            self.print_postorder(self.root)
            print()
        elif traversal_type.lower() == "preorder":
            self.print_preorder(self.root)
            print()
        else:
            print("Invalid Traversal Type, use: [inorder],[postorder],[preorder]")
    
    def print_inorder(self,node):
        if node:
            self.print_inorder(node.left)
            print (node.data, end=" ")
            self.print_inorder(node.right)
    
    def print_postorder(self,node):
        if node:
            self.print_postorder(node.left)
            self.print_postorder(node.right)
            print(node.data, end=" ")

    def print_preorder(self,node):
        if node:
            print(node.data, end =" ")
            self.print_preorder(node.left)
            self.print_preorder(node.right)

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

    def search(self,tar_data):
        if self.root is None:
            return False
        return self._search(self.root, tar_data)
    
    def _search(self, node, tar_data):

        if node is None:
            found = False
        else:
            if tar_data == node.data:
                found = True
            if tar_data < node.data:
                found = self._search(node.left, tar_data)
            if tar_data > node.data:
                found = self._search(node.right, tar_data)
        return found

    def is_leaf(self, node):
        if node.left is None and node.right is None:
            return True
        else:
            return False

    def min_value_of_tree(self,node):
        curr_node = node
        while curr_node.left is not None:
            curr_node = curr_node.left
        return curr_node

    def delete(self, node, tar_data):
        if self.root is None:
            raise Exception("Empty Tree!")
        if node is None:
            return node
        if tar_data < node.data:
            node.left = self.delete(node.left,tar_data)
        elif tar_data > node.data:
            node.right = self.delete(node.right,tar_data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            
            temp = self.min_value_of_tree(node.right)
            node.data = temp.data
            node.right = self.delete(node.right, temp.data)
        return node

bst = BST()

bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)



print("Inorder: ")
bst.print_tree("INorder")
print("Postorder: ")
bst.print_tree("postorder")
print("Preorder: ")
bst.print_tree("preorder")
print("Delete 20")
bst.delete(bst.root,20)
bst.print_tree("INorder")
print("Delete 30")
bst.delete(bst.root,30)
bst.print_tree("INorder")
print("Delete 50")
bst.delete(bst.root,50)
bst.print_tree("INorder")
print("Delete 40")
bst.delete(bst.root,40)
bst.print_tree("INorder")
print("Delete 70")
bst.delete(bst.root,70)
bst.print_tree("INorder")
print("Delete 80")
bst.delete(bst.root,80)
bst.print_tree("INorder")



