from app.services import is_courier_available


def test_courier_available():
    assert is_courier_available("доступен") is True


def test_courier_busy():
    assert is_courier_available("занят") is False


def test_courier_offline():
    assert is_courier_available("не_в_сети") is False