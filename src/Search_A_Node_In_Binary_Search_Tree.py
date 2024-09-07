## Search_A_Node_In_Binary_Search_Tree.py
"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""
def search_node_in_bst(root, value):
    """
    Args:
     root(BinaryTreeNode_int32)
     value(int32)
    Returns:
     bool
    """
    def is_pres(nde, val):
        if nde is None:
            return False
        elif nde.value == val:
            return True
        elif val < nde.value:
            return is_pres(nde.left, val)
        else:
            return is_pres(nde.right, val)
    
    
    return is_pres(root, value)