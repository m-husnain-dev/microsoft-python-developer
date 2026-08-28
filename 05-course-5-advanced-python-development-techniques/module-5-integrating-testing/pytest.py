import pytest


# 1. Low-level module: Database Connection
class Database:

    def __init__(self):
        self._data = {}

    def save(self, key, value):
        self._data[key] = value

    def get(self, key):
        return self._data.get(key)


# 2. High-level module: User Service
class UserService:

    def __init__(self, db: Database):
        self.db = db

    def register_user(self, user_id, name):
        if not name:
            raise ValueError("Name cannot be empty")
        # Direct interaction with Database module
        self.db.save(user_id, {"name": name, "active": True})

    def get_user_profile(self, user_id):
        return self.db.get(user_id)


# ==========================================
# INTEGRATION TEST (using pytest)
# ==========================================


@pytest.fixture
def test_db():
    # Real database/state initialization for integration
    db = Database()
    return db


def test_user_service_database_integration(test_db):
    """Integration Test: Validates interaction between UserService and

    Database.
    """
    service = UserService(test_db)

    # Action: Service call
    service.register_user("user_101", "Ali")

    # Verification: Checking state in Database via Service
    profile = service.get_user_profile("user_101")

    assert profile is not None
    assert profile["name"] == "Ali"
    assert profile["active"] is True