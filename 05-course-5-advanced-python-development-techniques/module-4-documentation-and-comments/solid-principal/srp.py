# GOOD: Single Responsibility
class UserProfile:

    def __init__(self, name: str):
        self.name = name


class DatabaseLogger:

    def save_user(self, user: UserProfile):
        print(f"Saving {user.name} to Database...")