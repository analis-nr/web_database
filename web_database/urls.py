from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('home', include('home.urls')),
    path('', include('impor_exim.urls')),
    path('', include('ekspor_exim.urls')),
]
