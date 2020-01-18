''' datetime library for get time '''
from datetime import datetime
from django.shortcuts import render
import requests
from .models import Item
from .forms import PriceSelection
from django.db.models import Count
items = []
response_buy = requests.get('https://market.csgo.com/history/json/')


def index(request):
    sort = False
    sort_items_form = PriceSelection()
    for i in range(0, 50, 1):
        items.append(response_buy.json()[i]['hash_name'] + ',,' + str(response_buy.json()[i]['price']))
    items.sort()
    popular_items = list(items)
    for i in popular_items:
        item = Item(name=i.split(',,')[0], price=i.split(',,')[1], url_icon='https://cdn.csgo.com/item/'+ i.split(',,')[0] +'/300.png')
        item.save()
    counts_item = Item.objects.values('name', 'price', 'url_icon').annotate(sell_count=Count('name')).distinct()
    date_now = datetime.now()
    if request.GET:
        sort = True
        date_now = datetime.now()
        min_price = request.GET.get('min_value')
        max_price = request.GET.get('max_value')
        sorted_price = Item.objects.filter(price__range=[min_price, max_price])
        data = {'sorted_items': sorted_price, 'sort': sort, 'time_now': date_now}
        return render(request, 'index.html', data)
    data = {'sort_items_form': sort_items_form, 'time_now': date_now, 'counts_item': counts_item}
    return render(request, 'index.html', data)
