from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.usuario_lista, name='lista'),
    path('crear/', views.usuario_crear, name='crear'),
    path('<int:pk>/', views.usuario_detalle, name='detalle'),
    path('<int:pk>/editar/', views.usuario_editar, name='editar'),
    path('<int:pk>/eliminar/', views.usuario_eliminar, name='eliminar'),
]
