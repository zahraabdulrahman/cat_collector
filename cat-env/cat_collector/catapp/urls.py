from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.catapp, name='catapp'),
    path('review/', views.review, name='review'),
]
