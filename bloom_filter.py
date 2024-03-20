import sys
import math
from hash_func import HashFunc
import pickle

class BloomFilter:
    def __init__(self, words_size=500000, probability=0.01, filter_size=None, number_of_hash_func=None, bf_data=None):
        self.int_size = 8
        if not filter_size:
            self.size = self.calculate_optimal_bloom_filter_size(words_size, probability)
        else:
            self.size = filter_size * self.int_size
        if not number_of_hash_func:
            self.number_of_hash_functions = self.calculate_number_of_hash_functions(self.size, words_size)
        else:
            self.number_of_hash_functions = number_of_hash_func
        if not bf_data:
            self.bloom_filter = bytearray([0] * math.ceil(self.size / self.int_size))
        else:
            self.bloom_filter = pickle.loads(bf_data)
        self.hash_funcs = self.get_hash_functions()


    def get_hash_functions(self):
        hash_funcs = []
        for i in range(self.number_of_hash_functions):
            hash_funcs.append(HashFunc('salt' + str(i)))
        return hash_funcs
    

    def calculate_optimal_bloom_filter_size(self, n, p):
        m = - (n * math.log(p)) / (math.log(2) ** 2)
        return math.ceil(m)

    def calculate_number_of_hash_functions(self, m, n):
        k = (m / n) * math.log(2)
        return math.ceil(k)
    

    def get_hash_value_index(self, hash_val):
        return hash_val % math.ceil(self.size / self.int_size)

    def add(self, element):
        for func in self.hash_funcs:
            hash_val = func.hash_md5(string=element)
            hash_val = self.get_hash_value_index(hash_val)
            index, bit_index = self.find_index_and_bit(hash_val)
            self.bloom_filter[index] = self.bloom_filter[index] | (1 << bit_index)
    
    def find_index_and_bit(self, hash_val):
        index = hash_val // self.int_size
        bit_index = hash_val % self.int_size
        return index, bit_index    

    def exists(self, element):
        for func in self.hash_funcs:
            hash_val = func.hash_md5(element)
            hash_val = self.get_hash_value_index(hash_val)
            index, bit_index = self.find_index_and_bit(hash_val)
            if not self.bloom_filter[index] & (1 << bit_index):
                return False
        return True
