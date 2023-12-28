class Users:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def has_password(self):
        return hash(self.password)


u1 = Users('John Doe', 'agl@455')
u2 = Users('Ella Doe', 'admin1234')
print(u1.has_password)
print(u2.__hash__())
