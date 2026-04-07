import hashlib
import math

class BloomFilter:
    def __init__(self, m, k):
        if m <= 0:
            raise ValueError("m must be positive")
        if k <= 0:
            raise ValueError("k must be positive")
            
        self.m = m
        self.k = k
        self.bit_array = [0] * m

        # Use hashlib algorithms (system-dependent)
        self.hash_algorithms = hashlib.algorithms_available
        self.hash_functions = []

        for algorithm in self.hash_algorithms:
            try:
                if 'shake' in algorithm:
                    self.hash_functions.append(
                        lambda x, a=algorithm: int(hashlib.new(a, x.encode()).hexdigest(8), 16)
                    )
                else:
                    self.hash_functions.append(
                        lambda x, a=algorithm: int(hashlib.new(a, x.encode()).hexdigest(), 16)
                    )
            except (ValueError, TypeError):
                continue

        if k > len(self.hash_functions):
            raise ValueError("k is larger than available hash functions")

        self.n_elements = 0  # number of items inserted

    def add(self, item):
        for i in range(self.k):
            idx = self.hash_functions[i](item) % self.m
            self.bit_array[idx] = 1
        self.n_elements += 1

    def contains(self, item):
        for i in range(self.k):
            idx = self.hash_functions[i](item) % self.m
            if self.bit_array[idx] == 0:
                return False
        return True

    # -------------------------------
    # Helper methods for bloom filter math
    # -------------------------------

    @staticmethod
    def optimal_k(m, n):
        """Compute the optimal number of hash functions for given m and n"""
        if n == 0:
            return 1
        return max(1, round((m / n) * math.log(2)))

    @staticmethod
    def required_m(n, epsilon):
        """Compute the required number of bits m for n elements and false positive probability epsilon"""
        if epsilon <= 0 or epsilon >= 1:
            raise ValueError("epsilon must be between 0 and 1")
        return math.ceil(- (n * math.log(epsilon)) / (math.log(2) ** 2))

    @staticmethod
    def false_positive_probability(m, n, k):
        """Compute approximate false positive probability"""
        if m <= 0 or n <= 0 or k <= 0:
            return 1.0
        return (1 - math.exp(-k * n / m)) ** k

    def current_false_positive(self):
        """Compute approximate false positive probability with current parameters and elements inserted"""
        return self.false_positive_probability(self.m, self.n_elements, self.k)

    @staticmethod
    def goel_gupta_bound(m, n, k):
        """Rigorous upper bound for false positive probability (finite filter)"""
        if m <= 1 or n < 0 or k <= 0:
            return 1.0
        return (1 - math.exp(-k * (n + 0.5) / (m - 1))) ** k
