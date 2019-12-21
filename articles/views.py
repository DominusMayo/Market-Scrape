''' datetime library for get time '''
from datetime import datetime
from django.shortcuts import render
import requests
from .models import Item
from .forms import PriceSelection
items = []
errors = []
response_buy = requests.get('https://market.csgo.com/history/json/')


def index(request):
    sort = False
    sort_items_form = PriceSelection()
    for i in range(0, 50, 1):
        items.append(response_buy.json()[i]['hash_name'] + ',,' + str(response_buy.json()[i]['price']))
    items.sort()
    popular_items = list(set(items))
    for i in popular_items:
        item = Item(name_item=i.split(',,')[0], price_item=i.split(',,')[1], url_icon='https://cdn.csgo.com/item/'+ i.split(',,')[0] +'/300.png')
        item.save()
    name_item = Item.objects.all()
    count_items = len(name_item)
    date_now = datetime.now()
    if request.GET:
        min_price = request.GET.get('min_value')
        max_price = request.GET.get('max_value')
        sort = True
        sorted_price = Item.objects.filter(price_item__range=[min_price, max_price])
        sorted_count_items = len(sorted_price)
        data = {'name': name_item, 'count_items' : count_items, 'sort_items_form': sort_items_form,
                'sorted_items': sorted_price, 'sort': sort,
                'sorted_items_price': sorted_count_items, 'time_now': date_now}
        return render(request, 'index.html', data)
    data = {'items': name_item, 'count_items': count_items,
            'sort_items_form': sort_items_form, 'time_now': date_now}
    return render(request, 'index.html', data)
