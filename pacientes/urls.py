from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.paciente_lista, name='lista'),
    path('crear/', views.paciente_crear, name='crear'),
    path('<int:pk>/', views.paciente_detalle, name='detalle'),
    path('<int:pk>/editar/', views.paciente_editar, name='editar'),
    path('<int:pk>/eliminar/', views.paciente_eliminar, name='eliminar'),
]
