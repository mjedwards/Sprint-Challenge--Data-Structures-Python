class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amg = []
        self.cur = 0

    def append(self, item):
        # if self.amg:
        #     self.amg.append(item)
        # if len(self.amg) == 0:
        #     self.amg.append(item)

        # elif len(self.amg) == self.capacity:
        #     self.cur = 0
        #     self.amg[self.cur] = item
        #     self.cur = (self.cur) % self.capacity
        
        # elif len(self.amg)<self.capacity:
        #     self.amg.append(item)

        # else:
        #     self.amg[self.cur]=item
        #     self.cur=(self.cur)%self.capacity
            
    def get(self):
        return self.amg

        

print(RingBuffer(5).append(1))
# print(RingBuffer(5).append(2))
# print(RingBuffer(5).append(4))