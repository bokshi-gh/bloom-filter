from bloom_filter import BloomFilter

# Create Bloom filter
bf = BloomFilter(m=100, k=5)

# Add items
bf.add("apple")
bf.add("banana")

# Check items
print("apple:", bf.contains("apple"))    # True
print("banana:", bf.contains("banana"))  # True
print("grape:", bf.contains("grape"))    # False
print("orange:", bf.contains("orange"))  # False (might be True if collision)

