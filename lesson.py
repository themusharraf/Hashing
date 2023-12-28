import hashlib

data = "PDP SCHOOL"

hash_obj = hashlib.md5(str(data).encode('utf-8'))

print(hash_obj.hexdigest())

# c1e4a430ee63f8947535da5c0279a86f
