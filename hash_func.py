import hashlib


class HashFunc:
    def __init__(self, salt):
        self.salt = salt

    def hash_md5(self, string):
        string = string + self.salt
        hash_value = int(hashlib.md5(string.encode('utf-8')).hexdigest(), 16)
        return hash_value
