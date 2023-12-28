import hashlib

data = "PDP SCHOOL"

sha256 = hashlib.sha256(str(data).encode('utf-8'))
sha384 = hashlib.sha384(str(data).encode('utf-8'))
md5 = hashlib.md5(str(data).encode('utf-8'))
blake2b = hashlib.blake2b(str(data).encode('utf-8'))
sha1 = hashlib.sha1(str(data).encode('utf-8'))

hash_list: list = [sha256, sha384, md5, blake2b, sha1]
for x in hash_list:
    print(x.hexdigest())
