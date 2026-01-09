"""
MongoDB integration for Dealer and Review data
"""
import os
from pymongo import MongoClient

# MongoDB connection
MONGODB_URL = os.environ.get('MONGODB_URL', 'mongodb://localhost:27017/')
client = MongoClient(MONGODB_URL)
db = client['dealerships']
dealers_collection = db['dealers']
reviews_collection = db['reviews']


def get_dealers():
    """Get all dealers from MongoDB"""
    dealers = list(dealers_collection.find())
    for dealer in dealers:
        dealer['_id'] = str(dealer['_id'])
    return dealers


def get_dealer_by_id(dealer_id):
    """Get a specific dealer by ID"""
    dealer = dealers_collection.find_one({'id': int(dealer_id)})
    if dealer:
        dealer['_id'] = str(dealer['_id'])
    return dealer


def get_dealers_by_state(state):
    """Get dealers filtered by state"""
    dealers = list(dealers_collection.find({'state': state}))
    for dealer in dealers:
        dealer['_id'] = str(dealer['_id'])
    return dealers


def get_dealer_reviews(dealer_id):
    """Get reviews for a specific dealer"""
    reviews = list(reviews_collection.find({'dealership': int(dealer_id)}))
    for review in reviews:
        review['_id'] = str(review['_id'])
    return reviews


def add_review(review_data):
    """Add a new review to MongoDB"""
    result = reviews_collection.insert_one(review_data)
    return str(result.inserted_id)


def init_sample_data():
    """Initialize sample dealers and reviews"""
    # Check if data already exists
    if dealers_collection.count_documents({}) > 0:
        return
    
    # Sample dealers
    sample_dealers = [
        {
            'id': 1,
            'name': 'Premium Motors',
            'city': 'Kansas City',
            'state': 'Kansas',
            'address': '123 Main St',
            'zip': '66101',
            'lat': 39.0997,
            'long': -94.5786
        },
        {
            'id': 2,
            'name': 'AutoHub Central',
            'city': 'Topeka',
            'state': 'Kansas',
            'address': '456 Oak Ave',
            'zip': '66603',
            'lat': 39.0558,
            'long': -95.6890
        },
        {
            'id': 15,
            'name': 'Elite Car Sales',
            'city': 'Wichita',
            'state': 'Kansas',
            'address': '789 Elm St',
            'zip': '67202',
            'lat': 37.6872,
            'long': -97.3301
        },
    ]
    
    # Sample reviews
    sample_reviews = [
        {
            'id': 1,
            'dealership': 15,
            'name': 'John Smith',
            'purchase': True,
            'review': 'Fantastic services and great customer support!',
            'purchase_date': '2024-01-15',
            'car_make': 'Toyota',
            'car_model': 'Camry',
            'car_year': 2023
        },
        {
            'id': 2,
            'dealership': 15,
            'name': 'Jane Doe',
            'purchase': True,
            'review': 'Excellent experience, highly recommend.',
            'purchase_date': '2024-02-20',
            'car_make': 'Honda',
            'car_model': 'Accord',
            'car_year': 2023
        },
    ]
    
    dealers_collection.insert_many(sample_dealers)
    reviews_collection.insert_many(sample_reviews)
    print("Sample data initialized successfully!")
