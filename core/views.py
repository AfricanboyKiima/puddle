from django.shortcuts import render
from item.models import Category, Item

""""""
#index page
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6] #6 items to be retrieved from Item object, only the unsold ones
    categories = Category.objects.all()#retrieve all categories
    return render(request, 'core/index.html', {'categories':categories,'items':items,})


#contact page
def contact(request):
    return render(request, 'core/contact.html')