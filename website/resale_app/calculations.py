# Helper functions to reduce the size of views


def calculate_average_sale_price(data):
    if len(data)>0:
        average_sale_price = sum([int(x.sale_price) for x in data.iterator()])/len(data)
        return f"${average_sale_price:.2f}"
    return None
 
def calculate_range_sale_price(data):
    if len(data)>0:
        min_sale_price = min([int(x.sale_price) for x in data.iterator()])
        max_sale_price = max([int(x.sale_price) for x in data.iterator()])
        return f"${min_sale_price} to ${max_sale_price}"
    return None

def calculate_avg_list_price_reduction(data):
    if len(data)>0:
        avg_list_price_reduction = sum([int(x.list_price) - int(x.sale_price) for x in data.iterator() if x.list_price != '0'])/len(data)
        return f"${avg_list_price_reduction:.2f}"
    return None    

def calculate_eighty_percent(data):
    if len(data)>0:
        sorted_data_list = sorted([int(x.sale_price) for x in data.iterator()])
        eighty_percent_category = sorted_data_list[int(len(sorted_data_list)*0.8)]
        return f"${eighty_percent_category:.2f}"    
    return None