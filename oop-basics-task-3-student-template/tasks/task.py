class Counter:
    def __init__(self, start=0, stop=None):
        self.stop = stop
        self.cnt = start

    def increment(self):
        
        if self.stop is not None and self.cnt >= self.stop:
            return  'Maximal value is reached.'
        else:
            self.cnt = self.cnt + 1


    def get(self):
        return self.cnt
    

c = Counter(start=42, stop=43)
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
c.increment()
print(c.get())