"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the reversed linked list in the below method.
"""

def Reverse(head):
    current = head
    prev = None
    while current:
        if not current.next:
            newh = current
            current.next = prev
            return newh
        next = current.next
        current.next = prev
        prev = current
        current = next

