class Node:
    def __init__(self, key, val) -> None:
        self.key, self.val = key, val


class LRUCache:
    # Time: O(?)
    # Space: O(?)
    def __init__(self, capacity: int) -> None:
        self.cap = capacity
        self.cache = {}

        self.left_edge, self.right_edge = Node(0, 0), Node(0, 0)
        self.left_edge.next, self.right_edge.prev = self.right_edge, self.left_edge

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def add(self, node):
        prev, nxt = self.right_edge.prev, self.right_edge
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node

    # Time: O(?)
    # Space: O(?)
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].val
        return -1

    # Time: O(?)
    # Space: O(?)
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left_edge.next
            self.remove(lru)
            del self.cache[lru.key]
