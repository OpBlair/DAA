from collections import deque

class Queue:
    """Queue implementation using collections.deque."""
    def __init__(self):
        # deque is optimized for O(1) appends and pops from either end
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        """Adds an item to the rear (right side) of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Removes and returns the item from the front (left side) of the queue."""
        if not self.is_empty():
            return self.items.popleft() # O(1) operation
        raise IndexError("dequeue from empty queue")

    def peek(self):
        """Returns the item at the front without removing it."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("peek from empty queue")

# Example Usage
my_queue = Queue()
my_queue.enqueue("A")
my_queue.enqueue("B")
print(f"Front element: {my_queue.peek()}") # Output: A
print(f"Dequeued element: {my_queue.dequeue()}") # Output: A
print(f"Dequeued element: {my_queue.dequeue()}") # Output: B
