from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('user/new/', views.user_create, name='user_create'),
    path('user/<int:pk>/', views.user, name='user'),
    path('user/<int:pk>/edit/', views.user_edit, name='user_edit'),
    path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('user/<int:pk>/event/new/', views.event_create, name='event_create'),
    path('event/', views.event, name='event'),
    path('user/<int:pk>/event/edit/', views_event_edit, name='event_edit'),
    path('user/<int:pk>/event/delete/', views_event_delete, name='event_delete')
]


