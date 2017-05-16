"""
Finding the parent of a node given
the node and the head of the tree, recursive

and moving subtree to new parent, linear
"""


class Node:
    def __init__(self, data=None):
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)


def find_parent(node, head):
    """Returns parent node of a node,
    returns None if no parent, i.e. for head"""
    for child in head.children:
        if child == node:
            return head
        parent = find_parent(node, child)
        if parent:
            return parent
    return None


def move_subtree(node, head, target):
    """Moves node to become child of target,
    thereby moving node's subtree as well"""
    # find current parent of node and remove reference
    parent = find_parent(node, head)
    parent.children.remove(node)
    # add node to target node's children
    target.add_child(node)
    return None

