from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='Home'),
    # path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('reservations/', views.reservations, name='reservations'),
    path('detail/', views.detail, name='detail'),
    path('detail/<int:id>/', views.detail, name='detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)