from . import views
from django.urls import path

urlpatterns = [
    path('',views.movie_list,name='movie_list')
]
