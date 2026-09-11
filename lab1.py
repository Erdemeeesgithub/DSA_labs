def can_construct(word, letters):
    counts = [0] * 26
    
    for character in letters: 
        index = ord(character) - ord('a')
        counts[index] += 1
        
    for character in word:
        index = ord(character) - ord('a')
        counts[index] -= 1
        if counts[index] < 0:
            return False
        
    return True


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        new_a = self.a + other.a 
        new_b = self.b + other.b
        return Complex(new_a, new_b)
    def __sub__(self, other):
        new_a = self.a - other.a 
        new_b = self.b - other.b
        return Complex(new_a, new_b)
    def __mul__(self, other):
        new_a = self.a * other.a 
        new_b = self.b * other.b
        new_a2 = self.a * other.b
        new_b2 = self.b * other.a
        return Complex(new_a - new_b, new_a2 + new_b2)
    def __repr__(self):
        if self.b < 0:
            return str(self.a) + " - " + str(abs(self.b)) + "i"
        else:
            return str(self.a) + " + " + str(self.b) + "i"
        
    def __iadd__(self, other):
        self.a = self.a + other.a
        self.b = self.b + other.b
        return self
    
def create_permutation(n):
    pass