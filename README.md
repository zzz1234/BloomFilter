# Bloomfilter Project

The Bloomfilter project is a Python application that implements a Bloom filter to efficiently check if a word is a valid English word or not. It allows you to create a Bloom filter from a list of words and dump the filter into a binary file. Later, you can use this binary file to verify if a word or a line of words separated by spaces is a valid English word or not.

## Installation

To use the Bloomfilter project, you'll need Python installed on your system. Clone this repository and navigate to the project directory:

```bash
git clone <repository_url>
cd Bloomfilter
```

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

# Usage

## Creating a Bloom Filter

To create a Bloom filter, you can use the create_bloom_filter.py script with the following command line parameters:

```bash
python main.py --file <input_file> --binary_file <output_binary_file>

```

- `--file`: Path to the file containing a list of words (e.g., words.txt).
- `--binary_file`: Path to the binary file where the Bloom filter will be dumped.

Example:

```bash
python main.py --file words.txt --binary_file bloom_filter.bf
```

## Validating Words using Bloom Filter

To validate a line of words using the Bloom filter, you can use the validate_bloom_filter.py script with the following command line parameters:


```bash
python main.py --binary_file <input_binary_file> --line <words_to_check>
```

- `--binary_file`: Path to the binary file containing the Bloom filter.
- `--line`: Line of words separated by spaces to spell check.

Example:

```bash
python validate_bloom_filter.py --binary_file bloom_filter.bf --line "hello world example"
```

