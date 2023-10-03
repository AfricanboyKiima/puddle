from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
#The above imports are just for photo illustration but this should never be done in production  
############
from django.contrib import admin
from django.urls import path,include
from core.views import index,contact,landing
from item.views import detail

urlpatterns = [
    path('item/', include('item.urls')),
    path('index/',index,name='index'),
    path('contact/', contact, name='contact'),
    path('landing/', landing, name='landing'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
