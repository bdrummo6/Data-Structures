
class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        if self.storage:
            for val in self.storage:
                if val > value:
                    if not self.storage.index(val):
                        self.storage.append(value)
                    else:
                        self.insert(value)
                elif value > val:
                    self.storage.insert(self.storage.index(val), value)

        else:
            self.storage.append(value)

    def delete(self):
        pass

    def get_max(self):
        pass

    def get_size(self):
        pass

    def _bubble_up(self, index):
        pass

    def _sift_down(self, index):
        pass

mh = Heap()

mh.insert(11)
mh.insert(9)
mh.insert(17)
mh.insert(12)

print(mh.storage)



