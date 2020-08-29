class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amg = []
        # self.cur = -1

    def append(self, item):
        # if len(self.amg) == self.capacity:
        #     return self.amg

        # else:
        #     self.cur = (self.cur + 1) % self.capacity
        #     self.amg[self.cur] = self.amg.append(item)
        if len(self.amg) == self.capacity:
            return self.amg

        else:
            self.amg.append(item)
            
            

    def get(self):
        return self.amg

        