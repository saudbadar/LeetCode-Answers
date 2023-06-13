class SnapshotArray:
    def __init__(self, length: int):
        self.arr = dict()
        self.snapshot = []
        self.updated = True

    def set(self, index: int, val: int) -> None:
        self.arr[index] = val
        self.updated = True

    def snap(self) -> int:            
        if self.updated:
            self.snapshot.append({**self.arr})
        else:
            self.snapshot.append(self.snapshot[-1])
        self.updated = False
        return len(self.snapshot)-1

    def get(self, index: int, snap_id: int) -> int:
        return self.snapshot[snap_id].get(index, 0)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)