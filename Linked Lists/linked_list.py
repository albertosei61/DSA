class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        #Create new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #Print list method
    def print_list(self):
        temp = self.head
        while temp != None:
            print(temp.value)
            temp = temp.next

    #Appending to node        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

        


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()

