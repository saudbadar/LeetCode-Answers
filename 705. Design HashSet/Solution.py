class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.hashMap = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        loc = key % self.size
        if(key not in self.hashMap[loc]):
            self.hashMap[loc].append(key)

    def remove(self, key: int) -> None:
        loc = key % self.size
        try:
            self.hashMap[loc].remove(key)
        except ValueError:
            pass  # do nothing!

    def contains(self, key: int) -> bool:
        if(key in self.hashMap[key % self.size]):
            return(True)
        else:
            return(False)