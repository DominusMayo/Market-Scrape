from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from articles.models import Item
from articles.forms import PriceSelection
from django.db.models import Count


def index(request):
    sort_items_form = PriceSelection()
    counts_item = Item.objects.values('name', 'price', 'url_icon').annotate(sell_count=Count('name')).distinct()
    date_now = datetime.now()
    paginator = Paginator(counts_item, 25)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    data = {'sort_items_form': sort_items_form, 'time_now': date_now, 'counts_item': page_obj, 'number_page': page_obj,}
    return render(request, 'index.html', data)


def search(request):
        if request.method == 'GET':
            date_now = datetime.now()
            min_price = request.GET.get('min_value')
            max_price = request.GET.get('max_value')
            sorted_price = Item.objects.values('name', 'price', 'url_icon').annotate(sell_count=Count('name')).filter(price__range=[min_price, max_price]).distinct()
            paginator = Paginator(sorted_price, 25)
            page_number = request.GET.get("page")
            try:
                page_obj = paginator.get_page(page_number)
            except PageNotAnInteger:
                page_obj = paginator.get_page(1)
            except EmptyPage:
                page_obj = paginator.get_page(paginator.num_pages)
            data = {'sorted_items': page_obj,'time_now': date_now, 'number_page': page_obj }
            return render(request, 'search.html', data)