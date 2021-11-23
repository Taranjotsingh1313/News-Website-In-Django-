from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('search/',views.search,name='search'),
    path('category/<str:name>/',views.category,name='category')
]
