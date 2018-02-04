from django.urls import path

from . import views

app_name = 'sitewide'

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('mdc/', views.indexMDC, name='indexMDC'),
]
