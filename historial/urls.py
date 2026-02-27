from django.urls import path
from . import views

app_name = 'historial'

urlpatterns = [
    path('', views.historial_lista, name='lista'),
    path('crear/', views.historial_crear, name='crear'),
    path('<int:pk>/', views.historial_detalle, name='detalle'),
    path('<int:pk>/editar/', views.historial_editar, name='editar'),
    path('<int:pk>/eliminar/', views.historial_eliminar, name='eliminar'),
]
