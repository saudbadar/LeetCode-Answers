class ListNode:
    def __init__(self, key, value) -> None:
        self.key = key
        self.val = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.randNumber = 10000
        self.lst = [None] * self.randNumber
        

    def put(self, key: int, value: int) -> None:
        pos = key % self.randNumber
        if(not self.lst[pos]):
            self.lst[pos] = ListNode(key, value)
            return
        newLst = self.lst[pos]
        while(newLst):
            if(newLst.key == key):
                newLst.val = value
                return
            prev, newLst = newLst, newLst.next
        prev.next =  ListNode(key, value)
            
        

    def get(self, key: int) -> int:
        pos = key % self.randNumber
        newLst = self.lst[pos]
        while(newLst):
            if(newLst.key == key):
                return(newLst.val)
            newLst = newLst.next
        return(-1)

    def remove(self, key: int) -> None:
        pos = key % self.randNumber
        if(not self.lst[pos]):
            return
        newLst = self.lst[pos]
        if(newLst.key == key):
            self.lst[pos] = newLst.next
            return
        while(newLst.next):
            if(newLst.next.key == key):
                newLst.next = newLst.next.next
                return
            newLst = newLst.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)