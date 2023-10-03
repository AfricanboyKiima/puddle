from django.shortcuts import render
from item.models import Category, Item

""""""
#index page
def index(request):
    items = Item.objects.filter(is_sold=False)[:] #In SQL == SELECT * FROM Item WHERE is_sold = False LIMIT 6  
    categories = Category.objects.all()#retrieve all categories
    return render(request, 'core/index.html', {'categories':categories,'items':items,})


#contact page
def contact(request):
    return render(request, 'core/contact.html')

def landing(request):
    return render(request, 'core/landing.html')