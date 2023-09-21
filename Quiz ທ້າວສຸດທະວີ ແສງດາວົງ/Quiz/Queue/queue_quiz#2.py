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
items = [10 * i for i in range(1,10)]
for item in items:
    queue.enqueue(item)
    if (item // 10) % 2 == 0 :
        queue.dequeue()

print(queue.queue)

# Output : [50, 60, 70, 80, 90]