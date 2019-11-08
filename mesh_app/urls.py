from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('user/', views.profile_page, name='user'),
    path('user/<int:pk>/edit/', views.profile_edit, name='profile_edit'),
    #path('user/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('user/<int:pk>/event/new/', views.event_create, name='event_create'),
    # path('user/<int:pk>/event/edit/', views_event_edit, name='event_edit'),
    path('events/', views.event_browse, name='event_browse'),
    path('event/<int:event_pk>/', views.event_page, name='event_page'),
    # path('user/<int:pk>/event/delete/', views_event_delete, name='event_delete'),
    # path('user/<int:pk>/event/join', views.event_join, name='event_join'),
    path('about/', views.about_page, name='about'),
]


