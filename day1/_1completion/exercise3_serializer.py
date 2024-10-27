"""
Build a custom JSON serializer that allows manually serializing
a user object into a JSON-like string and deserializing it.
"""

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"User(name={self.name}, age={self.age}, email={self.email})"

def custom_serialize_user(user):
    """
    Manually serialize the User object into a JSON-like string.
    """
    return f'{{"name": "{user.name}", "age": {user.age}, "email": "{user.email}"}}'

def custom_deserialize_user(serialized_data):
    """
    Manually deserialize the JSON-like string back into a User object.
    """
    data = serialized_data.strip('{}').split(', ')
    data_dict = {}
    for item in data:
        key, value = item.split(': ')
        key = key.strip('"')
        if key == "age":
            value = int(value)
        else:
            value = value.strip('"')
        data_dict[key] = value
    return User(name=data_dict["name"], age=data_dict["age"], email=data_dict["email"])

# Example usage
if __name__ == "__main__":
    print("Code Completion[3] Custom User Serializer")

    user = User(name="Alice", age=30, email="alice@example.com")

    serialized_data = custom_serialize_user(user)
    print(f"Custom Serialized User: {serialized_data}")

    deserialized_user = custom_deserialize_user(serialized_data)
    print(f"Custom Deserialized User: {deserialized_user}")
