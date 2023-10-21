from django.shortcuts import render,get_object_or_404
from .models import Item

#view to give us details of each item we click in the index page
def detail(request,pk):#it receives an id(pk) as each item will be found through its pk
    item = get_object_or_404(Item,pk=pk)
    related_items  = Item.objects.filter(category = item.category, is_sold = False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {'item':item})