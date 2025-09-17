# Bloom Filter

This repository contains a Python implementation of [Bloom Filter](https://en.wikipedia.org/wiki/Bloom_filter), a space-efficient probabilistic data structure.

> A **Bloom Filter** is a **bit array of size `m`** with **`k` independent hash functions**.

> **False positives are possible:** Bloom filter may report an element is present when it is not.  
>
> **False negatives are impossible:** Elements that are added will always be reported as present.  

> It is a space-efficient probabilistic data structure used to test if an element is a member of a set, allowing for very fast membership queries with a high degree of accuracy but with the possibility of false positives (stating an element is present when it's not)

## Features

- Pure Python implementation.  
- Supports **k independent hash functions** using Python’s `hashlib`.
- Modular: `BloomFilter` class can be imported and reused.

## Usage

Example usage is provided in **`main.py`**. Simply check/run `main.py` to see how to create a Bloom filter, add elements, and check membership.

## References

- [Bloom Filter - Wikipedia](https://en.wikipedia.org/wiki/Bloom_filter)  
- [False Positives and False Negatives - Wikipedia](https://en.wikipedia.org/wiki/False_positives_and_false_negatives)
- [Python hashlib documentation](https://docs.python.org/3/library/hashlib.html)
