import random
import string
from datetime import datetime, timedelta

EXAMPLE_1 = """
Generate a dataset of user profiles for a social media platform.
Each user profile should have the following attributes:

    User ID (unique identifier).
    Name (first and last name).
    Username (alphanumeric, unique).
    Email address (unique).
    Bio (a short biography, up to 150 characters).
    Join Date (a random date in the past two years).
    Followers count (a random number between 0 and 5000).
    Following count (a random number between 0 and 3000).

Use AI to write a script that will generate this dataset for you.
"""

def generate_user_profiles(n=100):
    users = []
    for i in range(n):
        user_id = i + 1
        first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
        last_name = ''.join(random.choices(string.ascii_uppercase, k=5))
        username = f'{first_name.lower()}{last_name.lower()}{random.randint(1, 999)}'
        email = f'{username}@example.com'
        bio = ''.join(random.choices(string.ascii_letters + ' ', k=150))
        join_date = datetime.now() - timedelta(days=random.randint(0, 730))  # Random date in the last two years
        followers_count = random.randint(0, 5000)
        following_count = random.randint(0, 3000)
        
        users.append({
            'User ID': user_id,
            'Name': f'{first_name} {last_name}',
            'Username': username,
            'Email': email,
            'Bio': bio[:150],  # Ensure bio is up to 150 characters
            'Join Date': join_date.strftime('%Y-%m-%d'),
            'Followers count': followers_count,
            'Following count': following_count
        })

    return users

EXAMPLE_2 = """
Generate mock data for e-commerce transactions.
Each transaction should contain:

    Transaction ID (unique identifier).
    User ID (links to a user).
    Product name (e.g., "Smartphone", "Laptop", etc.).
    Quantity (a number between 1 and 10).
    Price per unit (a decimal number between 10.00 and 2000.00).
    Total price (calculated as quantity * price per unit).
    Transaction Date (a random date in the past year).
    Shipping address (e.g., "123 Main St, New York, NY").

Use AI to generate the data itself and validate the correctness and diversity of the generated data.
"""

def generate_transactions(n=100):
    products = ["Smartphone", "Laptop", "Headphones", "Tablet", "Monitor", "Keyboard", "Mouse", "Charger"]
    transactions = []
    for i in range(n):
        transaction_id = i + 1
        user_id = random.randint(1, 100)  # Link to a user
        product_name = random.choice(products)
        quantity = random.randint(1, 10)
        price_per_unit = round(random.uniform(10.00, 2000.00), 2)
        total_price = round(quantity * price_per_unit, 2)
        transaction_date = datetime.now() - timedelta(days=random.randint(0, 365))  # Random date in the past year
        shipping_address = f'{random.randint(100, 999)} {random.choice(["Main", "Elm", "Pine"])} St, {random.choice(["New York", "Los Angeles", "Chicago"])}'

        transactions.append({
            'Transaction ID': transaction_id,
            'User ID': user_id,
            'Product name': product_name,
            'Quantity': quantity,
            'Price per unit': price_per_unit,
            'Total price': total_price,
            'Transaction Date': transaction_date.strftime('%Y-%m-%d'),
            'Shipping address': shipping_address
        })

    return transactions

EXAMPLE_3 = """
Generate mock data for sensor readings from Internet of Things (IoT) devices.
Each sensor reading should include:

    Device ID (unique identifier for the device).
    Timestamp (date and time of the reading).
    Temperature (a float between -10.0 and 40.0 degrees Celsius).
    Humidity (a percentage between 0 and 100%).
    Battery level (a percentage between 0 and 100%).
    Status ("online" or "offline").

Use AI to generate the data and ensure that the values fall within the specified ranges.
"""

def generate_sensor_readings(n=100):
    sensor_readings = []
    for i in range(n):
        device_id = i + 1
        timestamp = datetime.now() - timedelta(minutes=random.randint(0, 1440))  # Random timestamp within the last day
        temperature = round(random.uniform(-10.0, 40.0), 2)
        humidity = random.randint(0, 100)
        battery_level = random.randint(0, 100)
        status = random.choice(["online", "offline"])

        sensor_readings.append({
            'Device ID': device_id,
            'Timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'Temperature': temperature,
            'Humidity': humidity,
            'Battery level': battery_level,
            'Status': status
        })

    return sensor_readings


if __name__ == "__main__":
    print("Mock Data[6]")

    print("Profiles")
    for profile in generate_user_profiles(2):
        print(profile)

    print("Transactions")
    for transaction in generate_transactions(2):
        print(transaction)

    print("Sensor Readings")
    for reading in generate_sensor_readings(2):
        print(reading)
