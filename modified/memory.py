class Memory:
    def __init__(self):
        self.storage={}
    def store(self,query,output):
        self.storage[query]=output
    def retrieve(self,query):
        return self.storage.get(query,None)  