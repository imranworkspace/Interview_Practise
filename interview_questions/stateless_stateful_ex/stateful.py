class Count:
    def __init__(self):
        self.count=0
    def increment(self):
        self.count+=1
        return self.count
    
counter = Count()
print(counter.increment()) # output 1
print(counter.increment()) # output 2