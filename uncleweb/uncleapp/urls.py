from django.urls import path
from uncleapp import views


urlpatterns = [
    path('',views.fnt_hola),
    path('ejemplo/', views.fnt_ejemplo),
]