class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


class Queue:
    # time: O(1), space: O(1)
    def __init__(self):
        # instead of a list, we use linkedlist.
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return " ".join(values)

    # time: O(1), space: O(1)
    def isEmpty(self):
        if self.linkedList.head == None:
            return True
        return False

    # time: O(1), space: O(1)
    def enqueue(self, value):
        newNode = Node(value)

        # if the queue is empty, both head and tail will point to the new node.
        # here both head and tail becomes a "Node" object.
        if self.isEmpty():
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    # time: O(1), space: O(1)
    def dequeue(self):
        if self.isEmpty():
            return "There is no node in the queue!"
        else:
            tempNode = self.linkedList.head

            # If only the last/one element is left
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next

            return tempNode

    # time: O(1), space: O(1)
    def peek(self):
        if self.isEmpty():
            return "There is no node in the queue!"
        else:
            return self.linkedList.head

    # time: O(1), space: O(1)
    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


if __name__ == "__main__":
    # Testing the Queue implementation
    customQueue = Queue()

    # 1. Test isEmpty on empty queue
    print(f"Is Queue empty? {customQueue.isEmpty()}")

    # 2. Test enqueue
    print("Enqueuing 10, 20, 30...")
    customQueue.enqueue(10)
    customQueue.enqueue(20)
    customQueue.enqueue(30)
    print(f"Current Queue: {customQueue}")

    # 3. Test peek
    print(f"Peek: {customQueue.peek()}")

    # 4. Test dequeue
    print(f"Dequeue: {customQueue.dequeue()}")
    print(f"Current Queue after 1st dequeue: {customQueue}")

    # 5. Test dequeue until empty
    print(f"Dequeue: {customQueue.dequeue()}")
    print(f"Dequeue: {customQueue.dequeue()}")
    print(f"Dequeue attempt on empty: {customQueue.dequeue()}")

    # 6. Test delete
    print("Enqueuing 40, 50...")
    customQueue.enqueue(40)
    customQueue.enqueue(50)
    print(f"Current Queue: {customQueue}")
    customQueue.delete()
    print(f"Queue after delete: {customQueue}-")
    print(f"Is Queue empty after delete? {customQueue.isEmpty()}")
