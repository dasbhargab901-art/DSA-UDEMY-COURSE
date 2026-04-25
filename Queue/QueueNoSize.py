class Queue:
    # time: O(1), space: O(1)
    def __init__(self):
        self.items = []  # queue by using normal python list

    def __str__(self):
        values = [str(x) for x in self.items]
        return "[" + ",".join(values) + "]"

    # time: O(1), space: O(1)
    def isEmpty(self):
        return len(self.items) == 0

    # time: O(1), space: O(1)
    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted in the Queue!"

    # time: O(n), space: O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There is no element to remove!"
        self.items.pop(0)
        return "The first element inserted was removed!"

    # time: O(1), space: O(1)
    def peek(self):
        if self.isEmpty():
            return "There is no element to peek!"
        return self.items[0]

    # time: O(1), space: O(1)
    def delete(self): # deletes the entire queue
        self.items = []
        return 'Queue Cleared!!'

customQueue = Queue()
customQueue.enqueue(4)  # First element. It will be removed first as well.
customQueue.enqueue(40)
customQueue.enqueue(15)

print(customQueue.isEmpty())
print(customQueue)

# print(customQueue.dequeue())
# print(customQueue)

customQueue.delete()
print(customQueue)
