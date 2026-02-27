from django.urls import path
from . import views

app_name = 'formulario_fuv'

urlpatterns = [
    path('', views.fuv_lista, name='lista'),
    path('buscar-run/', views.buscar_paciente_run, name='buscar_run'),
    path('crear/', views.fuv_crear, name='crear'),
    path('<int:pk>/', views.fuv_detalle, name='detalle'),
    path('<int:pk>/editar/', views.fuv_editar, name='editar'),
    path('<int:pk>/eliminar/', views.fuv_eliminar, name='eliminar'),
]
