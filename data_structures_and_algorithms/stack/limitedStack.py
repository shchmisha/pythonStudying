
class Stack():
    def __init__(self, size):
        self.size = size
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def isFull(self):
        if len(self.list) == self.size:
            return True
        else:
            return False
    
    def push(self, value):
        if self.isFull():
            print('full')
            return "stack is full"
        else:
            # self.list = self.list +[value]
            self.list.append(value)
            print('success')
            return "element added"

    def pop(self):
        if self.isEmpty():
            return 'list empty'
        else:
            # value = self.list[-1]
            # del self.list[-1]
            # return value
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return 'list empty'
        else:
            # value = self.list[-1]
            # del self.list[-1]
            # return value
            return self.list[len(self.list)-1].pop()
        
    def delete(self):
        self.list = None

stack = Stack(5)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)
stack.push(1)

print(stack.pop())
print(stack.list)

        
