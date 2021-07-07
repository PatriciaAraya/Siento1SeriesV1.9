from django.urls import path
from .views import home, series, series_netflix, serie_ficha, series_disney, series_amazon, contactanos, iniciar_sesion, registro, nosotros
 
urlpatterns = [
    path('', home, name="home"),
    path('series/<action>/<id>', series, name="series"),
    path('series_netflix', series_netflix, name="series_netflix"),
    path('series_disney', series_disney, name="series_disney"),
    path('series_amazon', series_amazon, name="series_amazon"),
    path('iniciar_sesion', iniciar_sesion, name="iniciar_sesion"),
    path('registro', registro, name="registro"),
    path('nosotros', nosotros, name="nosotros"),
    path('contactanos', contactanos, name="contactanos"),
    path('serie_ficha/<id>', serie_ficha, name="serie_ficha")
]
