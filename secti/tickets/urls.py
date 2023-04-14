
from django.contrib import admin
from django.urls import path, include
from tickets import views

app_name = 'tickets'


urlpatterns = [
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('manager/logout/', views.manager_logout, name='manager_logout'),
    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('create_ticket/', views.create_ticket, name='create_ticket'),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('manager/change_status/<int:ticket_id>/', views.change_status, name='change_status'),
    path('manager/closed_tickets/', views.closed_tickets, name='closed_tickets'),
    path('ticket/<int:ticket_id>/notes/', views.ticket_notes, name='ticket_notes'),
]

