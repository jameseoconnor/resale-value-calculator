import math

def calculate_average_sale_price(data):
    average_sale_price = sum([int(x.sale_price) for x in data.iterator()])/len(data)
    return f"${average_sale_price:.2f}"

 
def calculate_range_sale_price(data):
    min_sale_price = min([int(x.sale_price) for x in data.iterator()])
    max_sale_price = max([int(x.sale_price) for x in data.iterator()])
    return f"${min_sale_price} to ${max_sale_price}"


def calculate_avg_list_price_reduction(data):
    avg_list_price_reduction = sum([int(x.list_price) - int(x.sale_price) for x in data.iterator() if x.list_price != '0'])/len(data)
    return f"${avg_list_price_reduction:.2f}"