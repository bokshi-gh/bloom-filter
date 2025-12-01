import hashlib

class BloomFilter:
    def __init__(self, m, k) -> None:
        self.m = m
        self.k = k
        self.bit_array = [0] * m

        self.hash_algorithms = hashlib.algorithms_available
        self.hash_functions = []

        if k > len(self.hash_algorithms):
            raise ValueError("k is larger than available hash algorithms")

        for algorithm in self.hash_algorithms:
            try:
                if 'shake' in algorithm:
                    # shake requires digest length
                    self.hash_functions.append(lambda x, a=algorithm: int(hashlib.new(a, x.encode()).hexdigest(8), 16))
                else:
                    self.hash_functions.append(lambda x, a=algorithm: int(hashlib.new(a, x.encode()).hexdigest(), 16))
            except (ValueError, TypeError):
                # Skip unsupported algorithms
                continue

    def add(self, item):
        for i in range(self.k):
            idx = self.hash_functions[i](item) % self.m
            self.bit_array[idx] = 1

    def contains(self, item):
        for i in range(self.k):
            idx = self.hash_functions[i](item) % self.m
            if self.bit_array[idx] == 0:
                return False
        return True
