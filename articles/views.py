from datetime import datetime
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from .models import Item
from .forms import PriceSelection
from django.db.models import Count


def index(request):
    sort_items_form = PriceSelection()
    counts_item = Item.objects.values('name', 'price', 'url_icon').annotate(sell_count=Count('name')).distinct()
    date_now = datetime.now()
    data = {'sort_items_form': sort_items_form, 'time_now': date_now, 'counts_item': counts_item,}
    return render(request, 'index.html', data)


def search(request):
        date_now = datetime.now()
        min_price = request.GET.get('min_value')
        max_price = request.GET.get('max_value')
        sorted_price = Item.objects.values('name', 'price', 'url_icon').annotate(sell_count=Count('name')).filter(price__range=[min_price, max_price]).distinct()
        data = {'sorted_items': sorted_price,'time_now': date_now,}
        return render(request, 'search.html', data)