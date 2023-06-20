from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:#provides us with metadata about our category model
        """Meta data is data that provides us with information about other data"""
        ordering = ('name',)#allows us to order our data in ascending order as per what I've understood
        verbose_name_plural = 'Categories'

    def __str__(self):#Special method used to display the object
        return self.name
    

class Item(models.Model):
    category = models.ForeignKey(Category,related_name='items', on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null= True)
    price = models.FloatField()
    is_sold = models.BooleanField(default= False)
    image = models.ImageField(upload_to='items_images',blank=True,null= True)
    #on_delete=models.CASCADE means that when a user is deleted, even the items he creates are deleted
    created_by = models.ForeignKey(User, related_name = 'items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:#Meta data is meant to provide us with information about other data in this case our category
        ordering = ('name',)#To ensure that our items are well organised i.e in ascending orders

    def __str__(self):#Special method in python used to display the object hence useful in debugging our code
        return self.name