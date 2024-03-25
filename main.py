import os
import json

with open('products.json') as f:
    products = json.load(f)

product_map = {}

for product in products:
    product_map[product['sku']] = float(product['price'])

with open('discounts.json') as f:
    discounts = json.load(f)

discount_map = {}

for discount in discounts:
    discount_map[discount['key']] = float(discount['value'])

with open('orders.json') as f:
    orders = json.load(f)


def calculate():
    total_sales_before_discount = 0
    total_sales_after_discount = 0

    for order in orders:
        for item in order['items']:
            total_sales_before_discount += product_map[item['sku']] * item['quantity']
            total_sales_after_discount += product_map[item['sku']] * item['quantity'] * discount_map.get(order.get('discount', 1), 1)

    total_amount_lost_via_discount = total_sales_before_discount - total_sales_after_discount

    average_discount_per_customer = total_amount_lost_via_discount / len(orders)

    return {
        "total_sales_before_discount": round(total_sales_before_discount, 2),
        "total_sales_after_discount": round(total_sales_after_discount, 2),
        "total_amount_lost_via_discount": round(total_amount_lost_via_discount, 2),
        "average_discount_per_customer": round(average_discount_per_customer, 2)
    }


if __name__ == '__main__':
    result = calculate()
    print(result)
