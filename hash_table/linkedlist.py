#!python
import pdb

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []

        node = self.head  

        while node is not None: 

            items.append(node.data)

            node = node.next  

        return items  

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        if self.head is None:
            return True
        
        return False

    def length(self):
        """
        Return the length of this linked list by traversing its nodes.
        Running time: O(n)
        """
        if self.is_empty():
            return 0
        current_node = self.head
        count = 1
        while current_node.next != None:
            count += 1
            current_node = current_node.next
        return count
 

    def append(self, item):
        """
        Insert the given item at the tail of this linked list.
        Running time: O(1)
        """
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node

    def prepend(self, item):
        """
        Insert the given item at the head of this linked list.
        Running time: O(1)
        """
        new_node = Node(item)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.head = new_node

    def find(self, quality):
        """
        Return an item from this linked list satisfying the given quality.
        Running time: O(n)
        """

        current_node = self.head

        while current_node.data != quality:
            current_node = current_node.next
            if current_node is None:
                return None
        return current_node.data

    def delete(self, item):
        """
        Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(n)
        """
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.is_empty():
            raise ValueError('Item not found: {}'.format(item))

        if self.length() == 1:
            self.head = None
            self.tail = None
            return

        current_node = self.head

        while current_node.data != item:
            previous_node = current_node
            current_node = current_node.next

            if current_node is None:
                raise ValueError('Item not found: {}'.format(item))
        
        if current_node == self.head:
            self.head = current_node.next
            return

        if current_node == self.tail:
            self.tail = previous_node

            previous_node.next = None
            return

        previous_node.next = current_node.next




def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))
        print(ll)

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
