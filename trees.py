class Trees:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

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
    
    def check_height(self):
        if self.root is None:
            return 0
        else:
            return self.height(self.root)

    def height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        
        #Figure out when the branch has ended
        if node is None:
            return 0
        
        else:
            # check left branches to see if they continue by using a recursive call
            left = self.height(node.left)

            # check the right branches to see if they continue by using a recursive call
            right = self.height(node.right)

            # Use max() to find the longest branch
            # return one for each layer as the recursive calls 'pass back'
            return max(left, right) + 1

tree = Trees()
tree.check_node(10)
tree.check_node(5)
tree.check_node(15)


print(tree.check_height())