import hashlib


def hashing(data):
    sha256 = hashlib.sha256(str(data).encode('utf-8'))
    return sha256.hexdigest()


print(hashing("@Aligator"))
