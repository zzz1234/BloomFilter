import argparse
import pickle
from bloom_filter import BloomFilter
import struct

def main(args):
    if args.file and args.binary_file:
        read_words_file_and_dump_binary(args.file, args.binary_file)
    
    elif args.binary_file:
        read_binary_file_and_spell_check(args.binary_file, args.line)


def read_binary_file_and_spell_check(file, line):
    with open(file, 'rb') as file:
        header = file.read(12)
        identifier, version, size, num_hash_func = validate_header(header)
        if identifier != b'CCBF':
            print("Invalid file format")
            return
        if version != 1:
            print("Unsupported version")
            return
        bf_data = file.read()
        b = BloomFilter(filter_size=size, number_of_hash_func=num_hash_func, bf_data=bf_data)
    
    print("Printing Words which do not exist in Bloom filter")
    for word in line.split():
        if not b.exists(word):
            print(word)


def validate_header(header):
    identifier, version, num_hash_func, size = struct.unpack('>4s H H I', header)
    return identifier, version, size, num_hash_func

def read_words_file_and_dump_binary(file, binary_file):
    with open(file, 'r') as file:
        data = file.read()
    b = BloomFilter()
    print("Addiing words to Bloom filter")
    for element in data.split():
        b.add(element)
    
    print("Dumping Bloom filter to binary file")
    serialized_bloom_filter = pickle.dumps(b.bloom_filter)
    dump_binary_file(serialized_bloom_filter, binary_file, 1, b.number_of_hash_functions, len(b.bloom_filter))


def dump_binary_file(bloom_filter, filename, version, num_hash_func, size):
    with open(filename, 'wb') as file:
        # Write the header
        header = struct.pack('>4s H H I', b'CCBF', version, num_hash_func, size)
        file.write(header)
        
        # Write the Bloom filter data
        file.write(bloom_filter)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Read a file')
    parser.add_argument('--file', dest='file', type=str, help='File to read')
    parser.add_argument('--binary_file', dest='binary_file', type=str, help='Binary file to read')
    parser.add_argument('--line', dest='line', type=str, help='Line to spell check')
    args = parser.parse_args()
    main(args)
