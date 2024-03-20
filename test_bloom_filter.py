import unittest

from bloom_filter import BloomFilter

class TestBloomFilter(unittest.TestCase):
    def setUp(self) -> None:
        self.bloom_filter = BloomFilter()
        return super().setUp()

    def test_false_negative(self):
        # We will insert two elements in the bloomfilter and then we will check for the element which is already present if it exists or not.
        # The Bloom filter will always return true.
        self.bloom_filter.add('hello')
        self.bloom_filter.add('world')
        self.assertTrue(self.bloom_filter.exists('hello'))
        self.assertTrue(self.bloom_filter.exists('world'))
    
    def test_negative(self):
        self.bloom_filter.add('hello')
        self.bloom_filter.add('world')
        self.assertFalse(self.bloom_filter.exists('bye'))
