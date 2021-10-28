from django.shortcuts import get_object_or_404, render
from django.db.models import Q

from .models import SoldItemsWomen
from .forms import SearchForm
from . import calculations as calc

def search_page(request):
    search_form = SearchForm()
    
    context = {
        "search_form": search_form
    }
    return render(request, 'resale_app/search_page.html', context)

# Brand: lululemon 
# Size: S
# Type: Pants_&_Jumpsuits

def search_result(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            garment_brand = form.cleaned_data['brand']
            garment_size = form.cleaned_data['size']
            garment_category = form.cleaned_data['category']

            data = SoldItemsWomen.objects.filter(
                Q(brand_name=garment_brand),
                Q(size=garment_size) | Q(category=garment_category)
            )
            graph_data = [int(x.sale_price) for x in data.iterator()]
            avg_sale_price = calc.calculate_average_sale_price(data)
            range_sale_price = calc.calculate_range_sale_price(data)
            avg_list_price_reduction = calc.calculate_avg_list_price_reduction(data)

            context = {
                "total_results": len(data),
                "graph_data": sorted(list(graph_data)),
                "avg_sale_price": avg_sale_price,
                "range_sale_price": range_sale_price,
                "avg_list_price_reduction": avg_list_price_reduction
            }

        else:
            context = {
                "search_result": False,
            }

    return render(request, 'resale_app/search_result.html', context)


