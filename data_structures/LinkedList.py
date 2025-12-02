class Node:
    """A node in a singly linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node, initialized to None

class LinkedList:
    """A Singly Linked List implementation."""
    def __init__(self):
        self.head = None

    # --- Core Operations ---

    def insert_at_beginning(self, data):
        """Adds a new node at the start of the list."""
        new_node = Node(data)
        new_node.next = self.head  # New node points to the current head
        self.head = new_node      # Head is updated to the new node

    def insert_at_end(self, data):
        """Adds a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        """Deletes the first node found with the given key (data value)."""
        current = self.head

        # Case 1: Node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None  # Free the node (optional but good practice)
            return

        # Case 2: Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # Key not found
        if current is None:
            print(f"Key '{key}' not found in the list.")
            return

        # Key found: Unlink the node from the list
        prev.next = current.next
        current = None

    def display(self):
        """Prints all elements in the list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    # --- Example Usage ---

# 1. Create a list
my_list = LinkedList()

# 2. Insert elements
my_list.insert_at_end(10)
my_list.insert_at_beginning(5)
my_list.insert_at_end(20)
my_list.insert_at_beginning(1)

print("Initial List:")
my_list.display()  # Output: 1 -> 5 -> 10 -> 20

# 3. Delete an element
my_list.delete_node(10)

print("\nList after deleting 10:")
my_list.display()  # Output: 1 -> 5 -> 20

# 4. Delete the head
my_list.delete_node(1)

print("\nList after deleting 1 (the head):")
my_list.display()  # Output: 5 -> 20