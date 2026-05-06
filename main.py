class User:
    def __init__(self, username):
        self.username = username


class Admin(User):
    def __init__(self, username, role):
        super().__init__(username)
        self._role = role

    def login(self):
        print("Login")

    def delete_user(self):
        print("User deleted")

    def ban_user(self):
        print("User banned")


a1 = Admin("Ali", "superadmin")

a1.login()
a1.delete_user()
a1.ban_user()
