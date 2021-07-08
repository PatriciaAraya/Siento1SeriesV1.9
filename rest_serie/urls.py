from django.urls import path
from django.contrib import admin
from .views import serie_create, serie_read, serie_read_all
from .views import serie_update, serie_delete, login

urlpatterns = [
    path('serie_create/', serie_create.as_view(), name="serie_create"),
    path('serie_update/', serie_update.as_view(), name="serie_update"),
    path('serie_read/<id>/', serie_read, name="serie_read"),
    path('serie_read_all/', serie_read_all, name='serie_read_all'),
    path('serie_delete/<id>/', serie_delete, name="serie_delete"),
    path('login', login, name='login'),
]