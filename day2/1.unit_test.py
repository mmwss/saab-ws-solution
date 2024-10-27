"""
Processes a list of orders and calculates the total price.
Each order contains multiple items. Each item is a dictionary with 'name', 'quantity', 'price', and 'discount'.
Handles edge cases such as missing fields, negative values, and invalid discounts.
"""

import unittest

def process_orders(orders):
    total_price = 0
    total_items = 0

    for order in orders:
        for item in order.get('items', []):
            name = item.get('name', '')
            quantity = item.get('quantity', 0)
            price = item.get('price', 0)
            discount = item.get('discount', 0)

            # Edge case handling: Skip items with invalid or negative values
            if quantity <= 0 or price <= 0 or discount < 0 or discount > 100:
                continue

            # Calculate price after discount
            item_price = quantity * price * (1 - discount / 100)
            total_price += item_price
            total_items += quantity

    # Apply bulk discount if total items exceed 100
    if total_items > 100:
        total_price *= 0.95  # Apply a 5% discount

    return total_price

class TestProcessOrders(unittest.TestCase):
    
    def test_normal_orders(self):
        orders = [
            {"items": [{"name": "item1", "quantity": 2, "price": 100, "discount": 10}]},
            {"items": [{"name": "item2", "quantity": 3, "price": 200, "discount": 0}]}
        ]
        result = process_orders(orders)
        expected = (2 * 100 * (1 - 10 / 100)) + (3 * 200 * (1 - 0 / 100))
        self.assertEqual(result, expected)

    def test_invalid_data(self):
        orders = [
            {"items": [{"name": "item1", "quantity": -2, "price": 100, "discount": 10}]},
            {"items": [{"name": "item2", "quantity": 3, "price": 200, "discount": 150}]},
            {"items": [{"name": "item3", "quantity": 3, "price": 0, "discount": 10}]}
        ]
        result = process_orders(orders)
        self.assertEqual(result, 0)

    def test_bulk_discount(self):
        orders = [
            {"items": [{"name": "item1", "quantity": 50, "price": 100, "discount": 10}]},
            {"items": [{"name": "item2", "quantity": 51, "price": 200, "discount": 0}]}
        ]
        result = process_orders(orders)
        total_items = 50 + 51
        expected = (50 * 100 * (1 - 10 / 100)) + (51 * 200 * (1 - 0 / 100))
        expected *= 0.95  # 5% discount for bulk order
        self.assertEqual(result, expected)

    def test_empty_orders(self):
        orders = []
        result = process_orders(orders)
        self.assertEqual(result, 0)

    def test_missing_fields(self):
        orders = [
            {"items": [{"name": "item1", "quantity": 2, "price": 100}]}  # Missing discount
        ]
        result = process_orders(orders)
        expected = 2 * 100  # No discount, just price * quantity
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        orders = [
            {"items": [{"name": "item1", "quantity": 1000000, "price": 100000, "discount": 50}]}
        ]
        result = process_orders(orders)
        expected = 1000000 * 100000 * (1 - 50 / 100)
        self.assertEqual(result, expected)

if __name__ == "__main__":
    print("Unit Test[1]")

    unittest.main()
