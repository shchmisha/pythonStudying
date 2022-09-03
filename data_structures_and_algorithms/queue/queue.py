
class Queue():
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    def enqueue(self, item):
        self.items.append(item)
        return 'item enqueued'

    def dequeue(self):
        if self.isEmpty():
            return 'queue empty'
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return 'queue empty'
        else:
            return self.items[0]

    def delete(self):
        self.items = None

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue)
