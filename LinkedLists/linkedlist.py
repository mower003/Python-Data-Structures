from collections import deque
#Linked List class definition
#creates head node
#Uses __repr__ as toString()
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data = nodes.pop())
            self.head = node
            for n in nodes:
                node.next = Node(data = n)
                node = node.next
    
    #Python's version of Java's toString()
    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    #Set starting node to head. While the node is not null, generate (yield acts like return, but creates a value that is only read once)
    #a node, and move the list to the next node.
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    #Inserts at the beginning of the list
    #Parameters: node to be inserted at the beginning
    #Make new node's next equal to current head then make current head equal to new node
    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head == None:
            self.head = node
            return
        for curr_node in self:
            pass
        curr_node.next = node

    def add_after(self, target_node, new_node):
        if self.head == None:
            raise Exception("Empty List")

        for n in self:
            if n.data == target_node:
                new_node.next = n.next
                n.next = new_node
                return
        raise Exception("target_node is not in the list")

    def add_before(self, target_node, new_node):
        if self.head == None:
            raise Exception("Empty List")

        if self.head.data == target_node:
            new_node.next = self.head
            self.head = new_node
        
        last_node_visited = self.head
        for n in self:
            if n.data == target_node:
                new_node.next = n
                last_node_visited.next = new_node
                return
            last_node_visited = n
        
        raise Exception("target_node is not in the list!")

    def remove_node(self, target_node):
        if self.head == None:
            raise Exception("Empty List")

        if self.head.data == target_node:
            self.head = self.head.next
            return
        
        last_node_visited = self.head
        for n in self:
            if n.data == target_node:
                last_node_visited.next = n.next
                return
        
        raise Exception("target_node is not in the list!")

    def get(self, index):
        if self.head == None:
            raise Exception("Empty List")

        if index == 0:
            return self.head.data
        
        count = 0
        for n in self:
            if index == count:
                return n.data
            count += 1

        raise Exception("Index out of bounds!")

    def reverse(self):
        if self.head == None:
            raise Exception("Empty List")

        previous_node = None
        current_node = self.head
        
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
        





        

#Node class definition
#Stores next node and data from instantiation
#Uses __repr__ as toString()
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

#Create linked list 'llist'
#head node is created and set to None
llist = LinkedList()
lllist = LinkedList(["Qualcomm","Viasat","Wilson, Towers & Watts", "Sony", "Blizzard","Intrepid Studios"])

#Create first_node and link head to first_node by assigning 'head' to first_node
first_node = Node("Terry")
llist.head = first_node
print(llist)
print(lllist)

#Create second and third nodes
second_node = Node("Peter")
third_node = Node("Carl")

#link first_node to second_node
#link second_node to third_node
first_node.next = second_node
second_node.next = third_node


print(llist)
for node in lllist:
    print(node)

lllist.add_first(Node("Google"))
print(lllist)
lllist.add_last(Node("Amazon"))
print(lllist)

llist3 = LinkedList()
print(llist3)
llist3.add_last(Node("Costco"))
print(llist3)
llist3.add_first(Node("Teradata"))
print(llist3)
llist3.add_after("Costco", Node("Viasat"))
print(llist3)
llist3.add_before("Costco", Node("Amazon"))
print(llist3)
llist3.remove_node("Amazon")
print(llist3)
llist3.add_first(Node("Qualcomm"))
print(llist3)
print(llist3.get(2))
print("Reverse Start: ")
llist3.reverse()
print(llist3)

lllist.reverse()
print(lllist)