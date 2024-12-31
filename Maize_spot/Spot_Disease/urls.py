from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('maize', views.MaizeView, basename='maize')

urlpatterns = [
    path('api/', include(router.urls))
    # path('', views.index, name='index'),
    # path('maize/', views.index, name='index'),
    # path('maize/<int:pk>/', views.maize_details, name='maize')
]