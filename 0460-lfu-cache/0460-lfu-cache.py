from collections import defaultdict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1

    def removeLast(self):

        if self.size == 0:
            return None

        node = self.tail.prev
        self.remove(node)

        return node


class LFUCache:

    def __init__(self, capacity):

        self.capacity = capacity
        self.minFreq = 0

        self.keyMap = {}
        self.freqMap = defaultdict(DLL)

    def updateFreq(self, node):

        freq = node.freq

        self.freqMap[freq].remove(node)

        if freq == self.minFreq and self.freqMap[freq].size == 0:
            self.minFreq += 1

        node.freq += 1

        self.freqMap[node.freq].add(node)

    def get(self, key):

        if key not in self.keyMap:
            return -1

        node = self.keyMap[key]

        self.updateFreq(node)

        return node.val

    def put(self, key, value):

        if self.capacity == 0:
            return

        if key in self.keyMap:

            node = self.keyMap[key]
            node.val = value

            self.updateFreq(node)

            return

        if len(self.keyMap) == self.capacity:

            node = self.freqMap[self.minFreq].removeLast()

            del self.keyMap[node.key]

        newNode = Node(key, value)

        self.keyMap[key] = newNode

        self.freqMap[1].add(newNode)

        self.minFreq = 1