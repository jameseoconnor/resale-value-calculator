import json 

from django.shortcuts import render
from django.http import Http404
from django.db.models import Q
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from .models import SoldItemsWomen
from .forms import SearchForm
from . import calculations as calc


def get_categories_available(request):
    brand = request.GET.get('brand', None)

    try:
        data = SoldItemsWomen.objects.values('category').distinct().filter(Q(brand_name=brand.upper()))
        data = [x['category'].replace("_", " ") for x in data]
        response = json.dumps(list(data), cls=DjangoJSONEncoder)

    except SoldItemsWomen.DoesNotExist:
        raise Http404("Given query not found....")

    return HttpResponse(response)


def search_page(request):
    available_brands = SoldItemsWomen.objects.values('brand_name').distinct()
    
    context = {
        "available_brands": available_brands
    }

    return render(request, 'resale_app/search_page.html', context)


def search_result(request):

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)  

        # check whether it's valid:
        if form.is_valid():
            garment_brand = form.cleaned_data['brand'].upper()
            garment_category = form.cleaned_data['category'].replace(" ", "_")
            # garment_keyword = form.cleaned_data['keyword']
            garment_keyword = 'test'

            data = SoldItemsWomen.objects.filter(
                Q(brand_name=garment_brand.upper()),    
                Q(category=garment_category),
            )

            graph_data = [int(x.sale_price) for x in data.iterator()]
            avg_sale_price = calc.calculate_average_sale_price(data)
            range_sale_price = calc.calculate_range_sale_price(data)
            avg_list_price_reduction = calc.calculate_avg_list_price_reduction(data)
            eighty_percent_category = calc.calculate_eighty_percent(data)

            context = {
                "garment_brand": garment_brand,
                "garment_category": garment_category.replace("_", " "),
                "total_results": len(data),
                "graph_data": sorted(list(graph_data)),
                "avg_sale_price": avg_sale_price,
                "range_sale_price": range_sale_price,
                "avg_list_price_reduction": avg_list_price_reduction,
                "eighty_percent_category": eighty_percent_category   
            }

            if garment_keyword is not None: 
                keyword_data = SoldItemsWomen.objects.filter(
                    Q(brand_name=garment_brand.upper()),
                    Q(category=garment_category),
                    Q(name__contains=garment_keyword.upper()),
                )
                
                keyword_avg_sale_price = calc.calculate_average_sale_price(keyword_data)
                keyword_range_sale_price = calc.calculate_range_sale_price(keyword_data)
                
                context.update({
                    "keyword": garment_keyword,
                    "keyword_data": keyword_data,
                    "keyword_total_results": len(keyword_data),
                    "keyword_avg_sale_price": keyword_avg_sale_price,
                    "keyword_range_sale_price": keyword_range_sale_price
                })

        else:
            context = {
                "search_result": False,
            }

    return render(request, 'resale_app/search_result.html', context)