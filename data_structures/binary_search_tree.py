class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # Insert a value
    def insert(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)
    
    def _insert(self, node, val):
        if val < node.val:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        elif val > node.val:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)
        # ignore duplicates
    
    # Search
    def search(self, val):
        return self._search(self.root, val)
    
    def _search(self, node, val):
        if not node or node.val == val:
            return node
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)
    
    # Delete a node (full implementation with three cases)
    def delete(self, val):
        self.root = self._delete(self.root, val)
    
    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node to delete found
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # Both children exist → replace with min from right subtree
            min_node = self._find_min(node.right)
            node.val = min_node.val
            node.right = self._delete(node.right, min_node.val)
        return node
    
    def _find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    # In-order traversal (sorted order)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)
