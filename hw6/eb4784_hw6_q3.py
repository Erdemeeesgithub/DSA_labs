from DoublyLinkedList import DoublyLinkedList


class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        for ch in orig_str:
            last = self.data.trailer.prev
            if last is self.data.header or last.data[0] != ch:
                self.data.add_last((ch, 1))
            else:
                last.data = (last.data[0], last.data[1] + 1)

    def add_run(self, letter, count):
        last = self.data.trailer.prev
        if last is self.data.header or last.data[0] != letter:
            self.data.add_last((letter, count))
        else:
            last.data = (letter, last.data[1] + count)

    def __add__(self, other):
        result = CompactString('')
        for letter, count in self.data:
            result.add_run(letter, count)
        for letter, count in other.data:
            result.add_run(letter, count)
        return result

    def compare(self, other):
        node1 = self.data.header.next
        node2 = other.data.header.next
        if node1 is not self.data.trailer:
            left1 = node1.data[1]
        if node2 is not other.data.trailer:
            left2 = node2.data[1]

        while node1 is not self.data.trailer and node2 is not other.data.trailer:
            if node1.data[0] != node2.data[0]:
                if node1.data[0] < node2.data[0]:
                    return -1
                return 1
            same = min(left1, left2)  
            left1 -= same
            left2 -= same
            if left1 == 0:
                node1 = node1.next
                if node1 is not self.data.trailer:
                    left1 = node1.data[1]
            if left2 == 0:
                node2 = node2.next
                if node2 is not other.data.trailer:
                    left2 = node2.data[1]

        if node1 is self.data.trailer and node2 is other.data.trailer:
            return 0
        if node1 is self.data.trailer:    
            return -1
        return 1

    def __lt__(self, other):
        return self.compare(other) < 0

    def __le__(self, other):
        return self.compare(other) <= 0

    def __gt__(self, other):
        return self.compare(other) > 0

    def __ge__(self, other):
        return self.compare(other) >= 0

    def __repr__(self):
        result = ''
        for letter, count in self.data:
            result += letter * count
        return result