
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="index"),
    path('contactus', views.contactus,name="contactus"),
    path('racingboots', views.racingboots,name="racing boots"),
    path('collection', views.collection,name= "collection"),
    path('shoes', views.shoes,name="shoes"),
]
