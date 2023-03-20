import datetime


def outdated_products(products: list) -> list:
    return [product["name"] for product in products
            if product["expire_date"] < datetime.date.today()]
