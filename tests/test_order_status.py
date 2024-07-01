import pytest
from modules.order_status import get_order_status, save_order_status

def test_save_order_status():
    assert save_order_status('12345', 'shipped') == True
    assert save_order_status('98765', 'processing') == True

def test_get_order_status_existing():
    assert get_order_status('12345') == "The status of your order ID 12345 is: shipped"
    assert get_order_status('98765') == "The status of your order ID 98765 is: processing"

def test_get_order_status_non_existing():
    assert get_order_status('99999') == "Sorry, we couldn't find an order with ID 99999. Please check your ID and try again."



if __name__ == "__main__":
    pytest.main()
