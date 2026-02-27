from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.reserva_lista, name='lista'),
    path('crear/', views.reserva_crear, name='crear'),
    path('<int:pk>/', views.reserva_detalle, name='detalle'),
    path('<int:pk>/editar/', views.reserva_editar, name='editar'),
    path('<int:pk>/eliminar/', views.reserva_eliminar, name='eliminar'),
]
