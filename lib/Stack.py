class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit


    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        return self.items

    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return None

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return True if len(self.items) == self.limit else False

    def search(self, target):
        if target in self.items:
            x = len(self.items)
            for item in self.items:
                if item == target:
                    dist = x  - (self.items.index(item) + 1)
                    return dist
        else:
            return -1
        
        
