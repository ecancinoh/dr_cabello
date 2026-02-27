from django.urls import path
from . import views

app_name = 'llegadas'

urlpatterns = [
    path('', views.llegada_lista, name='lista'),
    path('registrar/', views.llegada_registrar, name='registrar'),
    path('buscar-rut/', views.buscar_paciente_rut, name='buscar_rut'),
    path('<int:pk>/', views.llegada_detalle, name='detalle'),
    path('<int:pk>/editar/', views.llegada_editar, name='editar'),
    path('<int:pk>/eliminar/', views.llegada_eliminar, name='eliminar'),
]
