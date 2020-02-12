from articles.models import Item
from celery import task
import requests

@task
def adding_items_on_db():
    items = []
    response_buy = requests.get('https://market.csgo.com/history/json/')
    number_items = Item.objects.all().count()
    if number_items >= 9800:
        Item.objects.all().delete()
    else:
        for i in range(0, 50, 1):
            items.append(response_buy.json()[i]['hash_name'] + ',,' + str(response_buy.json()[i]['price']))
        items.sort()
        for i in items:
            item = Item(name=i.split(',,')[0], price=i.split(',,')[1], url_icon='https://cdn.csgo.com/item/'+ i.split(',,')[0] +'/300.png')
            item.save()   
