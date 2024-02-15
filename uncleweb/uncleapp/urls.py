from django.urls import path
from uncleapp import views


urlpatterns = [
    path('', views.fnt_inicio,name="inicio" ),
    path('juego1/', views.fnt_juego1, name='juego1')
]
