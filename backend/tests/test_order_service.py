from app.services import calculate_order_total, calculate_delivery_price


def test_calculate_order_total():
    items = [
        {"name": "Пицца", "price": 500, "quantity": 2},
        {"name": "Сок", "price": 100, "quantity": 1}
    ]

    result = calculate_order_total(items)

    assert result == 1100


def test_calculate_delivery_price():
    result = calculate_delivery_price(4)

    assert result == 200