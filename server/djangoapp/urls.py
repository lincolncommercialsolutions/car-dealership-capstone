from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('register', views.registration, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('get_user', views.get_user, name='get_user'),
    
    # Dealers
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<int:dealer_id>', views.get_dealership_by_id, name='get_dealer_by_id'),
    
    # Reviews
    path('get_reviews', views.get_reviews, name='get_reviews'),
    path('add_review', views.add_dealer_review, name='add_review'),
    
    # Cars
    path('get_cars', views.get_cars, name='get_cars'),
]
