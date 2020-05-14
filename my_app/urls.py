from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home),
    path('mov_res',views.mov_res),
]
