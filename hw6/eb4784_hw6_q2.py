from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.data = DoublyLinkedList()
        for ch in num_str:
            self.data.add_last(int(ch))
            
    def __add__(self, other):
        result = Integer('')
        cur1 = self.data.trailer.prev
        cur2 = other.data.trailer.prev
        carry = 0

        while cur1 is not self.data.header or cur2 is not other.data.header or carry != 0:
            d1 = 0
            if cur1 is not self.data.header:
                d1 = cur1.data
                cur1 = cur1.prev
            d2 = 0
            if cur2 is not other.data.header:
                d2 = cur2.data
                cur2 = cur2.prev

            total = d1 + d2 + carry
            result.data.add_first(total % 10)
            carry = total // 10

        return result
            
    def __repr__(self):
        result = ''
        for digit in self.data:
            result += str(digit)
        result = result.lstrip('0')    
        if result == '':
            result = '0'              
        return result