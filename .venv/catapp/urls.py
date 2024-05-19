from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.catapp, name='catapp'),
    path('review/', views.review, name='review'),
    path('game/', views.game, name='game'),
    path('game/firstCat/', views.firstCat, name='firstCat'),
    path('game/firstCat/secondCat', views.secondCat, name='secondCat'),
    path('game/firstCat/secondCat/thirdCat', views.thirdCat, name='thirdCat'),
    path('addCats/', views.addCat, name='addCat'),
    path('updateCat/<int:bId>', views.updateCat, name='updateCat'),
    path('filterCats', views.filterCats, name="filterCats")
]
