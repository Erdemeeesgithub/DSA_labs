import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self):
        self.data_arr = make_array(1)
        self.capacity = 1
        self.n = 0


    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data_arr[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data_arr[i]
        self.data_arr = new_array
        self.capacity = new_size


    def __getitem__(self, ind):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        return self.data_arr[ind]


    def __setitem__(self, ind, val):
        if (not (0 <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        self.data_arr[ind] = val


    def __iter__(self):
        for i in range(len(self)):
            yield self.data_arr[i]  #could also yield self[i]


    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)
            
    def __repr__(self):
        return '[' + ', '.join(repr(elem) for elem in self) + ']'
    
    def __add__(self, other):
        res = ArrayList()
        res.extend(self)
        res.extend(other)
        return res
 
    def __iadd__(self, other):
        self.extend(other)
        return self
 
    def __mul__(self, k):
        res = ArrayList()
        for _ in range(k):
            res.extend(self)
        return res
 
    def __rmul__(self, k):
        return self * k
 
    def remove(self, val):
        for i in range(self.n):
            if self.data_arr[i] == val:
                for j in range(i, self.n - 1):
                    self.data_arr[j] = self.data_arr[j + 1]
                self.data_arr[self.n - 1] = None
                self.n -= 1
                return
        raise ValueError('value not in list')
 
    def removeOdds(self):
        write = 0
        for read in range(self.n):
            if self.data_arr[read] % 2 == 0:
                self.data_arr[write] = self.data_arr[read]
                write += 1
        for i in range(write, self.n):
            self.data_arr[i] = None
        self.n = write
    