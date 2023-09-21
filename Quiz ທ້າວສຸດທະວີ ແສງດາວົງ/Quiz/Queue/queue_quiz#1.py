class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()
queue.enqueue("Banana")
queue.enqueue("Apple")
queue.enqueue("Tomato")
queue.dequeue()
queue.enqueue("Strawberry")
queue.enqueue("Grapes")
queue.dequeue()
print(queue.queue)

# Output : ['Tomato', 'Strawberry', 'Grapes']