from django.urls import path
from . import views

# https://docs.djangoproject.com/en/3.1/intro/tutorial03/#namespacing-url-names
app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('save/', views.save, name='save'),
]