class Count:
    def increment(self,value):
        self.count=value+1
        return self.count
    
counter = Count()
print(counter.increment(0)) # output 1
print(counter.increment(0)) # output 1, it will not increment