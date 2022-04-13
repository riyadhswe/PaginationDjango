
from django.contrib import admin
from django.urls import path,include
from App import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),
#    path('',views.movie_list,name='movie_list'),
]