import sys as system
import requests
import json
import decimal
import src.couriers as couriers

# generally not great practice to have a global...
default_items = [
    {"id": 4, "name": "Cold Brew", "price": 1.3},
    {"id": 3, "name": "Ginger Tea", "price": 1.2},
    {"id": 6, "name": "Water", "price": 1.0},
]
product_origin_codes = {
    "Cold Brew": "Italy",
    "Ginger Tea": "China",
    "Water": "France",
}
error_message = "is not an available option"


def get_first_courier():
    all_couriers = couriers.get_couriers()
    first_courier = all_couriers[0]
    return first_courier


def format_price(price):
    price_formatted = "{:.2f}".format(price)
    return price_formatted


def get_items(items=default_items):
    return items


def get_countries():
    headers = {"Content-Type": "application/json"}
    api_url = "https://restcountries.eu/rest/v2/all"

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None


# get user input for item they want to check
def products_origin_prompt():
    print("Which product do you want import information on?")
    selected_product = input()
    return selected_product


# retrieve country code for that product
def get_product_origin(product, product_origin_codes):
    product_origin = product_origin_codes[product]
    return product_origin


# call countries api for countries info
# retrieve country info using country code
def get_product_origin_info(product_origin, get_countries_function):
    countries = get_countries_function()
    for country in countries:
        if country["name"] == product_origin:
            print(country)
            result = f'Country: {product_origin}, Currency: {country["currencies"][0]["code"]}, Country Code: {country["alpha3Code"]}'
            return result


def get_product_origin_menu():
    selected_product = products_origin_prompt()
    origin = get_product_origin(selected_product, product_origin_codes)
    try:
        print(get_product_origin_info(origin, get_countries))
        return 1
    except Exception as e:
        print(e)


def get_origin_info_navigator():
    while get_product_origin_menu() != 1:
        pass


def get_item_index(name, items):
    item_index = next(
        (index for (index, item) in enumerate(items) if item["name"] == name)
    )
    return item_index


def update_item(updated_name, updated_price, product_to_update, items=default_items):
    item_index = get_item_index(product_to_update, items)
    product = items[item_index]
    product["name"] = updated_name
    product["price"] = updated_price

    print(
        f"Successfully updated {product_to_update} to {updated_name}, £{updated_price}!"
    )
    return items


def update_item_prompt():
    # needs validation on existence of product to be updated
    update_item_prompt = [
        "You are in the update items menu",
        "What's the name of the product you wish to update?",
    ]
    print("\n")
    print("\n".join(update_item_prompt))
    display_available_items(get_items(default_items))
    product_to_update = input()
    return product_to_update


def get_updated_item_name():
    # needs input validation
    updated_item_name_prompt = "Please enter the updated product name\n"
    name = input(updated_item_name_prompt)
    return name


def get_updated_item_price():
    # needs input validation on input length and type etc.
    updated_item_price_prompt = "Please enter the updated product price\n"
    price = input(updated_item_price_prompt)
    return convert_to_two_decimal_place(price)


def update_item_menu():
    # again, below three functions should probably
    # be composed into a single parent function
    # which would return the values in a collection
    product_to_update = update_item_prompt()
    name = get_updated_item_name()
    price = get_updated_item_price()

    try:
        update_item(name, price, product_to_update)
        return 1
    except Exception as e:
        print(e)


def update_item_navigator():
    while update_item_menu() != 1:
        pass


def add_item(new_item, items=default_items):
    items.append(new_item)
    formatted_price = format_price(new_item["price"])
    print(
        f"Successfully added {new_item['name']}, £{formatted_price} to the products list!"
    )
    return items


def get_new_item_name():
    new_item_name_prompt = "What's the name of the product you wish to add?\n"
    name = input(new_item_name_prompt)
    return name


def convert_to_two_decimal_place(price: str):
    # probably want more validation here
    decimal.getcontext().prec = 2
    return decimal.Decimal(price)


def get_new_item_price():
    new_item_price_prompt = "What's the price of the product you wish to add?\n"
    price = input(new_item_price_prompt)
    return convert_to_two_decimal_place(price)


def create_new_item(id, name, price):
    # hacky solution, do not emulate as it's not expressive at all
    new_product_dictionary = locals()
    return new_product_dictionary


def get_available_id(items=default_items):
    all_ids = [items["id"] for items in default_items]
    next_id = max(all_ids) + 1
    return next_id


def add_item_menu():
    # below needs input validation, validation against duplicating items
    # should combine below three functions in a parent function
    # probably called get_item_details()
    name = get_new_item_name()
    price = get_new_item_price()
    new_id = get_available_id()
    new_item = create_new_item(new_id, name, price)
    try:
        add_item(new_item, default_items)
        return 1
    except Exception as e:
        print(e)


def add_item_navigator():
    while add_item_menu() != 1:
        pass


def display_available_items(items):
    print("\nProducts:")
    for (
        index,
        item,
    ) in enumerate(items, 1):
        formatted_price = format_price(item["price"])
        print(index, f":: {item['name']} :: £ {formatted_price}")


def products_menu_prompt_and_choices():
    products_menu_prompt = ["You are in the products menu."]
    products_menu_choices = [
        "Enter 0 to return to the main menu",
        "Enter 1 to see all products",
        "Enter 2 to add a product",
        "Enter 3 to update a product",
        "Enter 4 to get a product's origin info",
        "Enter 5 to see an available courier",
    ]
    print("\n")
    print("\n".join(products_menu_prompt + products_menu_choices))


def products_menu(exit_menu_code):
    products_menu_prompt_and_choices()

    user_choice = input()
    leave_product_menu = user_choice == "0"
    show_items = user_choice == "1"
    add_item = user_choice == "2"
    update_item = user_choice == "3"
    get_item_origin_info = user_choice == "4"
    show_available_courier = "5"

    if show_items:
        display_available_items(get_items(default_items))
    elif add_item:
        add_item_navigator()
    elif update_item:
        update_item_navigator()
    elif get_item_origin_info:
        get_origin_info_navigator()
    elif leave_product_menu:
        return exit_menu_code
    elif show_available_courier:
        print(get_first_courier())
    else:
        print(user_choice, error_message)


def products_menu_navigation(menu_to_print):
    exit_code = 0
    while menu_to_print(exit_code) != exit_code:
        pass


def main_menu_prompt_and_choices():
    main_menu_prompt = ["You are in the main menu"]
    main_menu_options = [
        "Enter 1 to enter the products menu",
        "Enter 0 to exit the app",
    ]
    print("\n")
    print("\n".join(main_menu_prompt + main_menu_options))


def main_menu(exit_menu_code):
    main_menu_prompt_and_choices()

    user_choice = input()
    exit_app = user_choice == "0"
    leave_main_menu = user_choice == "1"

    if exit_app:
        system.exit("Byeee")
    elif leave_main_menu:
        return exit_menu_code
    else:
        print(user_choice, error_message)


def main_menu_navigation(menu_to_print):
    exit_code = 1
    while menu_to_print(exit_code) != exit_code:
        pass


def navigation():
    is_open = True
    while is_open:
        main_menu_navigation(main_menu)
        products_menu_navigation(products_menu)


def main():
    navigation()


if __name__ == "__main__":
    main()