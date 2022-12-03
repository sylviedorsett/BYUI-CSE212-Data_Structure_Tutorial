# Python Data Structure Tutorial
<hr/>
Welcome to my Data Structures Tutorial. This tutorial covers three data structures in Python. Each topic includes some instruction, examples and a practice problem.

1. [Home](welcome.md)
2. [Queues](queues.md)
3. [Trees](trees.md)

# Linked Lists:
<hr/>
    A Linked List in computer programming is a data structure similar to a dynamic array. Unlike a dynamic array whose items are stored in memory next to each other; the items of a Linked List can be stored randomly in a computer's memory. To keep the linked list together we must 'link' one item to the next item in the list. Each item is called a node. The first item in the linked list is called the head. The last item in the linked list is called the tail. Each link from one item to the next is called a pointer. Linked lists can have one pointer but most linked lists contain bi-directional linking. This means there are pointers connecting each node from Head to Tail and additional pointers connecting each node from Tail to Head.


One convenience of a Linked List is that you do not have to move items over in memory to be able to insert a new item into it. To insert a new item (node) into a Linked List we unchain the nodes to the left and right of where you want to put the new node and then chain (link) the new node to the nodes on its left and right.
    
## Real World Example:
<hr/>
    Consider a computer program that manages the order of an emergency room filled with patients. The staff has an ongoing list of patients to help, usually in order of first come first serve. However, when a patient of higher priorty arrives, they need to be inserted into the list. The computer program processing the patients can implement a linked list that unlinks patients in the linked list to insert new patients based on their priority.

## Linked Lists in Python
<hr/>
In Python we have several steps to take when creating nodes in a Linked List. It is best set up by creating a Linked List Class. The Linked List Class creates a Linked List Object. A Node Class can create a Node object that stores the information such as the previous and next nodes in the linked list; as well as the data that the node contains. For the examples below, assume we have created a class Node within another class Linked List. The node class contains data fields for 'next' and 'previous'.

Python provides a linked list called the 'deque' that you can import into your program. Though it includes several methods that make working with a linked list easier, it is important to understand how to insert and remove nodes from a linked list. 
    
To insert a new head to the list that already has a head we need to do the following:
1. Create a new node.
   **new_node = LinkedList.Node**
2. Make the current head of the linked list the 'next' node for the new node.
   **new_node.next = self.head**
3. Make the new node the previous node of the old head.
   **self.head.previous = new_node**
4. Make the new node the new head.
   **self.head = new_node**
    
To insert a new head to a list that is empty we need to do the following:
1. Create a new node.
   **new_node = LinkedList.Node**
2. Make the new node both the head and the tail of the linked list.
   **self.head = new_node**
   **self.tail = new_node**

To insert a new tail to a linked list that is not empty we need to do the following:
1. Create a new node.
   **new_node = LinkedList.Node**
2. Make the current tail the previous node to the new node.
   **new_node.previous = self.tail**
3. Make the next of the current tail the new node.
   **self.tail.next = new_node**
4. Make the new node the new tail.
   **self.tail = new_node**

To insert a new node into the middle of a linked list we need the current node you want to insert the new node after. Then do the following:
1. Create a new node.
   **new_node = LinkedList.Node**
2. Make the current node the 'previous' node to the new node
   **new_node.previous = current_node**
3. Make the next node in the linked list connect as 'next' for the new node.
   **new_node.next = current_node.next**
4. Make the new node the previous of the next node. 
   **current_node.next.previous = new_node**
5. Make the new node the next node for the current node.
   **current_node.next = new_node**

To remove a head node from a linked list we must do the following:
1. Set the previous of the next node to the head to a None value.
   **self.head.next.previous = None**
2. Set the next node in the linked list as the new head.
   **self.head = self.head.next**

To remove a tail node from a linked list we must do the following:
1. Set the next of the previous node to the tail to a None value.
   **self.tail.previous.next = None**
2. Set the previous node in the linked list as the new tail.
   **self.tail = self.tail.previous**

To remove a node from the middle of a linke list we must do the following:
1. Make the previous of the node you are removing the previous node to the next node in the linked list.
   **current_node.next.previous = current_node.previous**

2. Make the next of the node you are removing the next node to the previous node in the linke list.
   **current_node.previous.next = current_node.next**

## Big O Notation
<hr/>    
When using deque to work with linked lists the actions of inserting or removing a head or tail node, checking if the linked list is empty and getting the size of nodes in a linked list all have a Big O Notation of O(1). These operations have the same runtime regardless of the size of data in the linked list. When we insert or remove a node from the middle has a Big O Notation of O(n). Both of these operations require a loop to find the node. So as a linear performance, as the data increases, so does the performance.

## Example
<hr/>
    In the example below we will create a linked list and add three names to it.

    First we create a class named Linked List. The __init__ function will create self.head and self.tail data fields that will be set to None.

    Within the Linked List Class we will also create a Node class. The __init__ function will create data fields for self.name, self.next and self.previous.

```python
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
```

    We need to write functions in our Linked List class that will insert a new node as the head and tail.

```python
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
```

    We need to also write a function in our Linked List class that will insert a new node into the middle of a list after a specified node.

```python
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
```

    We can now create a Linked List Object from the Linked list class and add names to our Linked List using the following code:

```python
patients = LinkedList()
patients.insert_head(name="Alvin Chipmunk")
patients.insert_tail(name="Theodore Chipmunk")
patients.insert_middle(current_name="Alvin Chipmunk", name="Simon Chipmunk")
```

    We can display the results of our Linked List to confirm our names have been added to the Linked List.

```python
patients.printList()
#---------------------------------------------------------------------
/usr/local/bin/python3 /Users/Sylvie/Desktop/linked_list.py
Sylvie@Andrews-iMac ~ % /usr/local/bin/python3 /Users/Sylvie/Desktop/linked_list.py
Alvin Chipmunk
Simon Chipmunk
Theodore Chipmunk
Sylvie@Andrews-iMac ~ % 
```

## Problem to Solve
<hr/>
    In this problem you need to write code to remove the tail node from a linked list.

1. Using the code in the example above add a function to the Linked List Class that removes the tail node from a Linked list.

![Answer](linked_list.py)
    
