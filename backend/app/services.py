def calculate_order_total(items):
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    return total


def is_courier_available(courier_status):
    return courier_status == "доступен"


def calculate_delivery_price(distance_km):
    base_price = 100
    price_per_km = 25

    return base_price + distance_km * price_per_km