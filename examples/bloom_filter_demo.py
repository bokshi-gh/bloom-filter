from bloom_filter import BloomFilter

n = 1000
epsilon = 0.01
m = BloomFilter.required_m(n, epsilon)
k = BloomFilter.optimal_k(m, n)

bf = BloomFilter(m, k)
bf.add("apple")
bf.add("banana")

print("Contains 'apple'?", bf.contains("apple"))
print("Contains 'grape'?", bf.contains("grape"))
print("Current false positive estimate:", bf.current_false_positive())
print("Upper bound (Goel-Gupta):", BloomFilter.goel_gupta_bound(m, bf.n_elements, k))
