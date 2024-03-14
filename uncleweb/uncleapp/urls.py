from django.urls import path
from uncleapp import views


app_name = 'cursor'

urlpatterns = [
    path('', views.fnt_inicio,name="inicio" ),
    path('detalle/<str:nombre>', views.fnt_detalle, name='detalle'),
    path('unity/', views.fnt_unity, name='unity'),
    path('rpgmaker/', views.fnt_rpgmaker, name='rpgmaker')
]
