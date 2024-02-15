from django.urls import path
from . import views
from .api import pusher


urlpatterns = [
    path('', views.accounts, name='accounts'),
    path('destinations', views.destinations, name='destinations'),
    #path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    # Account Routes
    path('account/<int:pk>', views.view_account, name='view_account'),
    path('delete_account/<int:pk>', views.delete_account, name='delete_account'),
    path('add_account/', views.add_account, name='add_account'),
    path('update_account/<int:pk>', views.update_account, name='update_account'),

    # Destination Routes
    path('destination/<int:pk>', views.view_destination, name='view_destination'),
    path('delete_destination/<int:pk>', views.delete_destination, name='delete_destination'),
    path('add_destination/', views.add_destination, name='add_destination'),
    path('update_destination/<int:pk>', views.update_destination, name='update_destination'),

    # Destination Routes
    path('account_destinations/<int:pk>', views.account_destinations, name='account_destinations'),

    # API Endpoint
    path('server/incoming_data', pusher.incoming_data, name='incoming_data'),
]
