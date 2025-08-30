"""
Inorder traversal order:

Left subtree first
Root node second
Right subtree last

This is why it's called "inorder" - you process the root node "in" between processing the left and right subtrees.

Given the root of a binary tree, return the inorder traversal of its nodes' values.
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]
"""

def inorderTraversal_ver1(root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[int]
    """
    result = []

    def inorder(root):
        if not root:
            return

        inorder(root.left)
        result.append(root.val)
        inorder(root.right)
        return(result)

    inorder(root)
    return(result)

   def inorderTraversal_ver2(root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result