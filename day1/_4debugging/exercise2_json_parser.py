"""
Debug the program that reads data from a JSON file
but fails when the file does not contain the expected fields.

Sample user_data.json file: {
    "name": "Alice",
    "email": "alice@example.com"
}
"""

import json

def read_user_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        # Handle missing 'id' field gracefully
        user_id = data.get('id', None)  # Use .get() to avoid KeyError if 'id' is missing
        user_name = data.get('name', None)
        user_email = data.get('email', None)

        # Raise an exception if critical fields are missing
        if user_name is None or user_email is None:
            raise ValueError("Missing 'name' or 'email' field in the JSON data.")
        
    return user_id, user_name, user_email

# Example usage
if __name__ == '__main__':
    print("Code Debugging[2] JSON Parser")

    user_data_file = 'data/user_data.json'

    try:
        user_id, user_name, user_email = read_user_data(user_data_file)
        print(f"ID: {user_id}")
        print(f"Name: {user_name}")
        print(f"Email: {user_email}")
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except json.JSONDecodeError:
        print("Error: Failed to decode the JSON file.")
