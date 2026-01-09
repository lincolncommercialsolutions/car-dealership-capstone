"""
In-memory data storage for Dealer and Review data
NOTE: Replace with MongoDB when available
"""

# In-memory storage
dealers_data = []
reviews_data = []


def get_dealers():
    """Get all dealers from storage"""
    return dealers_data.copy()


def get_dealer_by_id(dealer_id):
    """Get a specific dealer by ID"""
    for dealer in dealers_data:
        if dealer.get('id') == int(dealer_id):
            return dealer
    return None


def get_dealers_by_state(state):
    """Get dealers filtered by state"""
    return [d for d in dealers_data if d.get('state') == state]


def get_dealer_reviews(dealer_id):
    """Get reviews for a specific dealer"""
    return [r for r in reviews_data if r.get('dealership') == int(dealer_id)]


def add_review(review_data):
    """Add a new review to storage"""
    review_id = len(reviews_data) + 1
    review_data['id'] = review_id
    reviews_data.append(review_data)
    return str(review_id)


def init_sample_data():
    """Initialize sample dealers and reviews"""
    global dealers_data, reviews_data
    
    # Check if data already exists
    if len(dealers_data) > 0:
        return
    
    # Sample dealers
    dealers_data.extend([
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
    ])
    
    # Sample reviews
    reviews_data.extend([
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
    ])
    
    print(f"Sample data initialized successfully!")
    print(f"Dealers: {len(dealers_data)}")
    print(f"Reviews: {len(reviews_data)}")
