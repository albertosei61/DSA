class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
        

    # WRITE FIND_MIDDLE_NODE METHOD HERE #
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow   
    #                                    #
    #                                    #
    #                                    #
    #                                    #
    ######################################

    # WRITE HAS_LOOP METHOD HERE #
    def has_loop(self):
        slow = self.head
        fast = self.head
        while fast !=None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                
                return True
        return False
    #                            #
    #                            #
    #                            #
    #                            #
    ##############################

    
#This is outside the class    
#### WRITE FIND_KTH_FROM_END FUNCTION HERE ####
def find_kth_from_end(ll, k):
    slow = ll.head
    fast = ll.head
    for _ in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow    




my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""

