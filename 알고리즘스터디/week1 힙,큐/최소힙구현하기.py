# 최소힙은 완전이진트리 즉, 배열을 이용해 구현할 수 있다
class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    # 삽입 시 부모 노드와 비교해서 작으면 자리 교체
    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = self.items[i], self.items[parent]
            i = parent
            parent = parent // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def _percolate_down(self, idx):
        left = idx * 2
        right = left + 1
        smallest = idx
        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right
        if smallest != idx:
            self.items[idx], self.items[smallest] = self.items[smallest], self.items[idx]
            self._percolate_down(smallest)

    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted


hq = BinaryHeap()
hq.insert(5)
hq.insert(10)
hq.insert(3)
hq.insert(7)
print(hq.extract())