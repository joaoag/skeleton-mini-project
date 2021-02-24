from io import StringIO
from unittest.mock import patch
from src import products


def test_get_items_returns_provided_collection():
    available_products = default_items = [
        {"id": 4, "name": "Cold Brew", "price": 1.3},
        {"id": 6, "name": "Water", "price": 1.0},
    ]
    expected = available_products

    actual = products.get_items(available_products)

    assert expected == actual


def test_add_item_adds_item_to_collection():
    available_products = [
        {"id": 1, "name": "Sprite", "price": 1.3},
        {"id": 8, "name": "Ginger Tea", "price": 1.2},
        {"id": 3, "name": "Coke", "price": 1.0},
    ]

    product_to_add = {"id": 9, "name": "Water", "price": 1.0}

    expected = [
        {"id": 1, "name": "Sprite", "price": 1.3},
        {"id": 8, "name": "Ginger Tea", "price": 1.2},
        {"id": 3, "name": "Coke", "price": 1.0},
        {"id": 9, "name": "Water", "price": 1.0},
    ]

    actual = products.add_item(product_to_add, available_products)

    assert expected == actual


def test_update_item_updates_item_inside_collection(monkeypatch):
    # Arrange
    available_products = [
        {"id": 1, "name": "Lemonade", "price": 1.3},
        {"id": 8, "name": "Coffee", "price": 1.2},
        {"id": 3, "name": "Tea", "price": 1.0},
    ]
    product_to_update = "Coffee"
    updated_product = "Water"
    updated_price = 0.9
    # updated_product_as_user_input = StringIO(updated_product)
    # monkeypatch.setattr("sys.stdin", updated_product_as_user_input)

    expected = updated_products = [
        {"id": 1, "name": "Lemonade", "price": 1.3},
        {"id": 8, "name": "Water", "price": 0.9},
        {"id": 3, "name": "Tea", "price": 1.0},
    ]

    # Act
    actual = products.update_item(
        updated_product, updated_price, product_to_update, available_products
    )

    assert actual == expected


def test_get_product_origin_returns_correct_origin():
    user_choice = "Cheese"
    expected = "Holland"
    stub_product_origin_codes = {"Cheese": "Holland"}

    actual = products.get_product_origin(user_choice, stub_product_origin_codes)

    assert expected == actual


def test_get_product_origin_info_returns_correct_information():
    # Arrange
    result = "Country: France, Currency: EUR, Country Code: FRA"
    expected = result
    stub_response = [
        {
            "name": "France",
            "alpha3Code": "FRA",
            "currencies": [{"code": "EUR", "name": "Euro", "symbol": "€"}],
        }
    ]

    def mock_get_countries():
        return stub_response

    actual = products.get_product_origin_info("France", mock_get_countries)
    assert actual == expected


@patch("src.couriers.get_couriers")
def test_get_first_courier_returns_first_courier_from_given_list(mock_couriers):
    mock_couriers.return_value = ["Bo", "Ao", "Jo"]
    expected = "Bo"
    actual = products.get_first_courier()
    assert expected == actual