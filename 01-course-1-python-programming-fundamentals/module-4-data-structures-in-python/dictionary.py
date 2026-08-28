# Creation
user = {"name": "Alice", "age": 25, "role": "Admin"}

# Operations
user["email"] = "alice@example.com"  # Add key-value
user["age"] = 26                     # Update value
user.pop("role")                     # Remove key

print(user) # Output: {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
