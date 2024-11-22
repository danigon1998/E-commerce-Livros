from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('catalog/', include('catalog.urls')),
]