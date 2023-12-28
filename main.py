import hashlib

# hashing functions
# print(hashlib.algorithms_available)

data = "PDP SCHOOL"
hash_obj = hashlib.md5(str(data).encode('utf-8'))

print(hash_obj.hexdigest())
