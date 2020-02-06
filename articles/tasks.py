from blog.celery import app
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import requests
from .models import Item
from .forms import PriceSelection
from django.db.models import Count
items = []
response_buy = requests.get('https://market.csgo.com/history/json/')


@app.task
def updatedb():
    number_items = Item.objects.all().count()
    if number_items >= 9063:
        number_items.delete()
    else:
        for i in range(0, 50, 1):
            items.append(response_buy.json()[i]['hash_name'] + ',,' + str(response_buy.json()[i]['price']))
        items.sort()
        for i in items:
            item = Item(name=i.split(',,')[0], price=i.split(',,')[1], url_icon='https://cdn.csgo.com/item/'+ i.split(',,')[0] +'/300.png')
            item.save()    
