class Stack:
    """Stack implementation using a Python list."""
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        """Adds an item to the top (end) of the list."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the item from the top (end) of the list."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("pop from empty stack")

    def peek(self):
        """Returns the item at the top without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("peek from empty stack")

# Example Usage
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
print(f"Top element: {my_stack.peek()}") # Output: 20
print(f"Popped element: {my_stack.pop()}") # Output: 20
print(f"Popped element: {my_stack.pop()}") # Output: 10
