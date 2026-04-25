class Queue:
    # time: O(1), space: O(n)
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return "[" + ",".join(values) + "]"

    # time: O(1), space: O(1)
    def isFull(self):
        if (self.top + 1 == self.start) or (
            self.start == 0 and self.top == self.maxSize - 1
        ):
            return True
        return False

    # time: O(1), space: O(1)
    def isEmpty(self):
        if self.start == -1:
            return True
        return False

    # time: O(1), space: O(1)
    def enqueue(self, value):
        if self.isFull():
            return "Queue is Full!"

        if self.isEmpty():
            self.start += 1

        self.top = (self.top + 1) % self.maxSize
        self.items[self.top] = value

        return "Value inserted"

    # time: O(1), space: O(1)
    def dequeue(self):
        if self.isEmpty():
            return "Nothing to POP!"

        removed_element = self.items[self.start]  # Save the value
        self.items[self.start] = None

        if self.start == self.top:  # If this was the last element
            self.start = -1
            self.top = -1
        else:
            self.start = (self.start + 1) % self.maxSize  # Wrap around!

        return removed_element  # Return the actual value
    
    # time: O(1), space: O(1)
    def peek(self):
        if self.isEmpty():
            return "Nothing to PEEK AT!"
        return self.items[self.start]

    # time: O(1), space: O(1)
    def delete(self):
        self.items = self.maxSize * [None]
        self.start = -1
        self.top = -1
        return "Queue Cleared!"


# 4 14 50 13
customQueue = Queue(5)

print(customQueue)
customQueue.enqueue(4)
customQueue.enqueue(14)
customQueue.enqueue(50)
customQueue.enqueue(13)
print(customQueue)

customQueue.dequeue()
print(customQueue)

customQueue.delete()
print(customQueue)
