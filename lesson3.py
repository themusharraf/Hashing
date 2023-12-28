import hashlib


def hashing(data: str):
    sha256 = hashlib.sha256(data.encode('utf-8'))
    return sha256.hexdigest()


print(hashing("@Aligator"))
