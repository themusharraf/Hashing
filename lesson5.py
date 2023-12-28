import hashlib

data: dict = {

    "username": "Anonymous",
    "password": "admin@33#"
}


def load_hesh(data):  # noqa
    for key in data.values():
        sha256 = hashlib.sha256(str(key).encode())

        with open("data.txt", "w") as file:
            txt = file.write(sha256.hexdigest())
            return txt


print(load_hesh(data))
