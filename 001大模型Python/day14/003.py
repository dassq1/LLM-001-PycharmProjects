"""
@Author:xuyinglai
@Date:2026/8/1
@DESC:
"""


def max_price_product(products):
    max_price = 0
    # max_product = None

    for name, price in products.items():

        if price > max_price:
            max_price = price
            max_product = name

    return max_product


products = {
    "苹果": 5,
    "香蕉": 3,
    "西瓜": 10,
    "葡萄": 8
}

result = max_price_product(products)

print("价格最高的商品:", result)
