from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('user/<int:pk>/', views.profile_page, name='user'),
    path('user/<int:pk>/edit/', views.profile_edit, name='profile_edit'),
    #path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('user/<int:pk>/event/new/', views.event_create, name='event_create'),
    # path('user/<int:pk>/event/edit/', views_event_edit, name='event_edit'),
    # path('event/', views.event),
    # path('event/<int:event_pk>/', views.event_detail, name='event_detail'),
    # path('user/<int:pk>/event/delete/', views_event_delete, name='event_delete')
    # path('user/<int:pk>/event/join', views.event_join, name='event_join')
]


