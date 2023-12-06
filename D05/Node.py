class Node:
    def __init__(self, name, child, destMinThresh, srcMinThresh, span):
        self.name = name
        self.child = child
        self.destMinThresh = destMinThresh
        self.srcMinThresh = srcMinThresh
        self.srcMaxThresh = srcMinThresh + span

    def is_in_range(self, val):
        return self.srcMinThresh <= val <= self.srcMaxThresh

    def convert(self, val):
        return val if val<self.srcMinThresh or val>self.srcMaxThresh else self.destMinThresh+(val-self.srcMinThresh)

    def get_child(self):
        return self.child

    def __str__(self):
        return f'(name:{self.name}, child:{self.child}, srcMin:{self.srcMinThresh}, srcMax:{self.srcMaxThresh}, destMin:{self.destMinThresh})'

    def __repr__(self):
        return self.__str__()