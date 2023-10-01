from django.urls import path
from . import views

urlpatterns = [
    # URL para listar todos los colegios
    path('schools/', views.school_list, name='school_list'),

    # URL para ver los detalles de un colegio específico
    path('schools/<int:school_id>/', views.school_detail, name='school_detail'),

    # URL para ver el mapa
    path('map/', views.map_view, name='map_view'),
]
