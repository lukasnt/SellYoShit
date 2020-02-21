from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('marketplace/', include('marketplace.urls')),
    path('checkserver/', index, name='index'),


]
