class LinkedList:
    """
    A class that creates a linked list.
    """

    class Node:
        """
        A class that creates a node in a linked list.
        """

        def __init__(self, name):
            self.name = name
            self.next = None
            self.previous = None
    
    def __init__(self):
        """
        Create an empty list
        """
        self.head = None
        self.tail = None

    def insert_head(self, name):
        """
        Insert a new head at the front of the linked list
        """
        new_node = LinkedList.Node(name)
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head # Connect new node to the previous head
            self.head.previous = new_node # Connect the previous head to the new node
            self.head = new_node      # Update the head to point to the new node

    def insert_tail(self, name):
        """
        Insert a new tail at the end of the linked list
        """
        # Create a new node
        new_node = LinkedList.Node(name)
        # If the linked list is empty, point both head and tail to the new node
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        # If the linked list is not empty, then only self.tail will be affected
        else:
            new_node.previous = self.tail   #Connect the new node to the current tail
            self.tail.next = new_node   #Connect the tail to the new node
            self.tail = new_node        #update the tail to point to the new node

    def insert_middle(self, current_name, name):
        """
        Insert a new node after the current name passed in.
        """
        #Start at the head of the list
        node = self.head
        while node is not None:
            if node.name == current_name:
                if node == self.tail:
                    self.insert_tail(name)
                else:
                    # Create a new node
                    new_node = LinkedList.Node(name)
                    new_node.previous = node       # Connect new node to the current node
                    new_node.next = node.next  # Connect new node to the node after 'current'
                    node.next.previous = new_node  # Connect node after 'current' to the new node
                    node.next = new_node       # Connect the node containing 'current' to the new node
                return
            node = node.next #go to the next node in line to search for current_name

    def remove_head(self):
        """ 
        Remove the head of the linked list.
        """
        # Check to see if the list has only one item in it set the head and tail to None creating an empty list.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has multiple nodes in it, then the only the head node will be affected.
        elif self.head is not None:
            self.head.next.previous = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    def remove_tail(self):
        """
        Remove the last tail of the linked list.
        """
        # Check to see if the list has only one item in it set the head and tail to None creating an empty list.
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # If the list has multiple nodes in it, then only the tail node will be affected.
        elif self.tail is not None:
            self.tail.previous.next = None  # Disconnect the tail from the second-to-last node
            self.tail = self.tail.previous  # Update the second-to-last node to be the new tail

    def remove(self, name):
        """
        Remove a node from a linked list that is not the head or tail.
        """
        """
        Remove the first node that contains 'value'.
        """
        # Create a variable set to the head node to search through the list
        node = self.head

        # Create a while loop that continues as long as the current node is not 'None'
        while node is not None:
            # Check to see if the data of the current node is equal to the value passed into the function
            if node.name == name:
                # If the node is the head call remove head function
                if node == self.head:
                    self.remove_head()
                elif node == self.tail:
                    self.remove_tail()
                else:
                    node.next.previous = node.prev  # Set the previous of the node after current to the node before current
                    node.previous.next = node.next  # Set the next of the node before current to the node after current
                return  #Exit the function after we remove
            # Increment the current node to the next node   
            node = node.next    

    def printList(self):
        """
        Loop through a linked list.
        """
        node = self.head
        while node is not None:
            print(node.name)
            node = node.next

patients = LinkedList()
patients.insert_head(name="Alvin Chipmunk")
patients.insert_tail(name="Theodore Chipmunk")
patients.insert_middle(current_name="Alvin Chipmunk", name="Simon Chipmunk")

patients.printList()



