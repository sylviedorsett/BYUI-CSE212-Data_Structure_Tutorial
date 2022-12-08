# Python Data Structure Tutorial
<hr/>
Welcome to my Data Structures Tutorial. This tutorial covers three data structures in Python. Each topic includes some instruction, examples and a practice problem.

1. [Home](welcome.md)
2. [Queues](queues.md)
3. [Linked Lists](LinkedLists.md)

# Trees:
<hr/>
A tree in computer programming is a data structure similar to a linked list that contains nodes that are connected with pointers. A tree gets its name from the shape it creates when it is mapped out. A tree starts with a root node. The root node can have multiple nodes connected to it, unlike a linked list. Nodes in a tree have parent-child relationships. The root node is a parent node while the subsequent nodes underneath it are called child nodes. The bottom nodes are called leaf nodes. Subtrees are formed when child nodes become parent nodes as child nodes are inserted beneath them to their left or right.

There are multiple types of Trees. A Binary Search Tree follows rules for the data that is placed into the tree by comparing the data of the parent node. If a child node's data value is less than the data value contained in a parent node, then the child node is inserted into the tree to the left of the parent node. If a child node's data value is more than the data value contained in the parent node, then the child node is inserted into the tree to the right of the parent node. If a child node's data value is equivalent to the data value contained in the parent node, then the child node can be inserted in either the left or the right slot of the parent node. So data sorted as it is stored in a Binary Search Tree.

A Balanced Binary Search Tree is a Binary Search Tree that is balanced or restructured as data is insterted into the tree so that it will always be balanced. For a tree to be balanced there cannot be a difference of height of more than one level from any path. The height of a tree can be found by counting the longest path from the root node to a leaf node.


## Real World Example:
<hr/>
Consider a database containing thousands of files. You need to find a particular file. If your files are stored in a data structure such as a Balanced Binary Search Tree, you can easily find that file in record time.

## Trees in Python
<hr/>
Python does not have a Binary Search Tree Class. To implement a tree data structure in Python you will need to create a Tree Class with a function to initialize a root node. There are many functions you can include in your class. A few you will want to consider including in your class are functions to insert and remove nodes, traverse through the tree, check the height of a tree, check to see if the if a particular node exists within a tree.

Various developers have created libraries with functions for Binary Search Trees. One of these can be found at https://pypi.org/project/bintrees/. However, understanding how to write these functions is valuable and should be understood prior to implementing these libraries. A few of the functions you can find include:

1. Inserting a value into a tree.
```python
insert(value) 
```
2. Removing a value from a tree.
```python
remove(value)
```
3. Checking to see if a value is in a tree.
```python
contains(value)
```
4. Visit all objects in the tree from smallest to largest.
```python
traverse_forward()
```
5. Visit all objects in the tree from largest to smallest.
```python
traverse_reverse()
```
6. Get the height of the tree.
```python
height(node)
```
7. Get the size of the tree.
```python
size()
```
8. Check to see if a tree is empty.
```python
empty()
```

## Big O Notation
<hr/>    
The benefits of a binary search tree can be seen when we look at the Big O notation for operations in a tree, especially when considering databases with large amounts of data. Operations such as inserting or removing a value into a tree or checking a tree to see if it contains a specific value have the Big O notation of O(log n) which is Logarithmic time. This means that while the size of data increases exponentially, the time only increases linearly. So the time it takes to process the data in a binary search tree increases fractionally while the data of the tree increases exponentially.

The operations to traverse a binary search tree or check the height of a node have a Big O notation of O(n) because their performance increases as the size of the tree increases.

The operations to get the size of a binary search tree or check if a tree is empty have a Big O notation of O(1) because they operate in constant time. This means th execution of these operations and the time it takes to process them do not depend on the size of data in the tree.

## Example
<hr/>
In the example below we will create a Trees class. From this class we will create a trees object and insert three nodes containing numbers into it.

First we create a class named Tree. The __init__ function will create a data field for the root node. The Tree class will also contain a subclass called Node. The Node class will contain an __init__ function that creates data fields for data, left, and right.

```python
class Trees:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
```
Next we will write a function that checks to see if a root node exists. If it does then that function will call an insert function. The insert function inserts a new node into the binary search tree using recursive calls to traverse the tree to find the proper sorted location in the tree. 

```python
    def check_node(self, data):
        if self.root is None:
            self.root = Trees.Node(data)
        else:
            self.insert(data, self.root)

    def insert(self, data, node):
        #Base Case - if the data is == node.data then just return and do not 
        if data == node.data:
            return

        else:
            if data < node.data:
                # The data belongs on the left side.
                if node.left is None:
                    # We found an empty spot
                    node.left = Trees.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the left sub-tree.
                    self.insert(data, node.left)
            else:
                # The data belongs on the right side.
                if node.right is None:
                    # We found an empty spot
                    node.right = Trees.Node(data)
                else:
                    # Need to keep looking.  Call _insert
                    # recursively on the right sub-tree.    
                    self.insert(data, node.right)
```

Now create an object of the Trees Class and add three nodes containing the numbers 10, 5, and 15.

```python
tree = Trees()
tree.insert(10)
tree.insert(5)
tree.insert(15)
```

## Problem to Solve
<hr/>
    Using the code in the example above add code to check the height of a binary search tree.

1. Write a function called 'check_height' that checks to see if the root node is None. If it is, return 0. Otherwise call a function called 'height'.
2. Write the 'height' function. This function will first check to see if the node is None and return 0. Otherwise it will use recursive calls to continue traversing through the branches of the tree until it has reached the longest leaf node.
3. Print the height of the tree by calling the 'check_height' function.
![Answer](trees.py)