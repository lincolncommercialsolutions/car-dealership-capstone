from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .models import CarMake, CarModel
from .restapis import (
    get_dealers, 
    get_dealer_by_id, 
    get_dealers_by_state,
    get_dealer_reviews,
    add_review
)


@csrf_exempt
def registration(request):
    """User registration endpoint"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            email = data.get('email')
            
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists'}, status=400)
            
            # Create user
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            
            return JsonResponse({
                'userName': username,
                'status': 'Registered successfully'
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'POST method required'}, status=400)


@csrf_exempt
def login_user(request):
    """User login endpoint"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return JsonResponse({
                    'userName': username,
                    'status': 'Authenticated'
                })
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'POST method required'}, status=400)


def logout_user(request):
    """User logout endpoint"""
    logout(request)
    return JsonResponse({'userName': '', 'status': 'Logged out'})


def get_user(request):
    """Get current logged-in user information"""
    if request.user.is_authenticated:
        return JsonResponse({
            'userName': request.user.username,
            'firstName': request.user.first_name,
            'lastName': request.user.last_name,
            'email': request.user.email,
            'isAuthenticated': True
        })
    else:
        return JsonResponse({
            'userName': None,
            'isAuthenticated': False
        })


def get_cars(request):
    """Get all car makes and models"""
    car_makes = CarMake.objects.all()
    cars_list = []
    
    for make in car_makes:
        make_dict = {
            'id': make.id,
            'name': make.name,
            'description': make.description,
            'models': []
        }
        for model in make.models.all():
            make_dict['models'].append({
                'id': model.id,
                'name': model.name,
                'type': model.car_type,
                'year': model.year,
                'dealer_id': model.dealer_id
            })
        cars_list.append(make_dict)
    
    return JsonResponse(cars_list, safe=False)


def get_dealerships(request):
    """Get all dealerships or filter by state"""
    state = request.GET.get('state')
    
    if state:
        dealers = get_dealers_by_state(state)
    else:
        dealers = get_dealers()
    
    return JsonResponse(dealers, safe=False)


def get_dealership_by_id(request, dealer_id):
    """Get a specific dealership by ID"""
    dealer = get_dealer_by_id(dealer_id)
    
    if dealer:
        return JsonResponse(dealer)
    else:
        return JsonResponse({'error': 'Dealer not found'}, status=404)


def get_reviews(request):
    """Get reviews for a dealer"""
    dealer_id = request.GET.get('dealerId')
    
    if not dealer_id:
        return JsonResponse({'error': 'dealerId parameter required'}, status=400)
    
    reviews = get_dealer_reviews(dealer_id)
    return JsonResponse(reviews, safe=False)


@csrf_exempt
def add_dealer_review(request):
    """Add a new review for a dealer"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Get sentiment from microservice
            review_text = data.get('review', '')
            sentiment_url = 'http://localhost:5000/analyze/' + review_text
            
            try:
                sentiment_response = requests.get(sentiment_url, timeout=5)
                sentiment = sentiment_response.json().get('sentiment', 'neutral')
            except:
                sentiment = 'neutral'
            
            # Add sentiment to review data
            data['sentiment'] = sentiment
            
            # Save review
            review_id = add_review(data)
            
            return JsonResponse({
                'status': 'Review added successfully',
                'review_id': review_id,
                'sentiment': sentiment,
                'dealership': data.get('dealership')
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'POST method required'}, status=400)
