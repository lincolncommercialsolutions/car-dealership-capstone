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
    
    # Sample dealers across multiple states
    dealers_data.extend([
        {
            'id': 1,
            'name': 'Premium Motors',
            'city': 'Kansas City',
            'state': 'Kansas',
            'address': '123 Main St',
            'zip': '66101',
            'lat': 39.0997,
            'long': -94.5786,
            'cars': ['Toyota Camry', 'Honda Accord', 'Ford F-150', 'Chevrolet Silverado']
        },
        {
            'id': 2,
            'name': 'AutoHub Central',
            'city': 'Topeka',
            'state': 'Kansas',
            'address': '456 Oak Ave',
            'zip': '66603',
            'lat': 39.0558,
            'long': -95.6890,
            'cars': ['BMW 3 Series', 'Mercedes-Benz C-Class', 'Audi A4', 'Tesla Model 3']
        },
        {
            'id': 3,
            'name': 'Elite Car Sales',
            'city': 'Wichita',
            'state': 'Kansas',
            'address': '789 Elm St',
            'zip': '67202',
            'lat': 37.6872,
            'long': -97.3301,
            'cars': ['Nissan Altima', 'Hyundai Sonata', 'Mazda CX-5', 'Subaru Outback']
        },
        {
            'id': 4,
            'name': 'Luxury Auto Gallery',
            'city': 'Austin',
            'state': 'Texas',
            'address': '100 Congress Ave',
            'zip': '78701',
            'lat': 30.2672,
            'long': -97.7431,
            'cars': ['Porsche 911', 'Jaguar F-Type', 'Range Rover', 'Lexus LS']
        },
        {
            'id': 5,
            'name': 'Valley View Motors',
            'city': 'Phoenix',
            'state': 'Arizona',
            'address': '250 Desert Rd',
            'zip': '85001',
            'lat': 33.4484,
            'long': -112.0740,
            'cars': ['Jeep Wrangler', 'Ram 1500', 'Dodge Charger', 'Chrysler Pacifica']
        },
        {
            'id': 6,
            'name': 'Sunshine Auto Center',
            'city': 'Miami',
            'state': 'Florida',
            'address': '500 Ocean Drive',
            'zip': '33139',
            'lat': 25.7617,
            'long': -80.1918,
            'cars': ['Chevrolet Corvette', 'Ford Mustang', 'Dodge Challenger', 'Toyota Supra']
        },
        {
            'id': 7,
            'name': 'Mountain Peak Autos',
            'city': 'Denver',
            'state': 'Colorado',
            'address': '1200 Mountain Blvd',
            'zip': '80202',
            'lat': 39.7392,
            'long': -104.9903,
            'cars': ['Subaru Forester', 'Toyota 4Runner', 'Honda CR-V', 'Mazda CX-9']
        },
        {
            'id': 8,
            'name': 'Coastal Motors',
            'city': 'San Diego',
            'state': 'California',
            'address': '800 Beach Blvd',
            'zip': '92101',
            'lat': 32.7157,
            'long': -117.1611,
            'cars': ['Tesla Model S', 'Rivian R1T', 'Lucid Air', 'Polestar 2']
        },
    ])
    
    # Sample reviews for multiple dealers
    reviews_data.extend([
        {
            'id': 1,
            'dealership': 1,
            'name': 'John Smith',
            'purchase': True,
            'review': 'Fantastic services and great customer support!',
            'purchase_date': '2024-01-15',
            'car_make': 'Toyota',
            'car_model': 'Camry',
            'car_year': 2023,
            'sentiment': 'positive'
        },
        {
            'id': 2,
            'dealership': 1,
            'name': 'Sarah Johnson',
            'purchase': True,
            'review': 'Excellent experience, highly recommend!',
            'purchase_date': '2024-02-20',
            'car_make': 'Honda',
            'car_model': 'Accord',
            'car_year': 2023,
            'sentiment': 'positive'
        },
        {
            'id': 3,
            'dealership': 2,
            'name': 'Mike Davis',
            'purchase': True,
            'review': 'Amazing luxury car selection and professional staff.',
            'purchase_date': '2024-03-10',
            'car_make': 'BMW',
            'car_model': '3 Series',
            'car_year': 2024,
            'sentiment': 'positive'
        },
        {
            'id': 4,
            'dealership': 3,
            'name': 'Emily Wilson',
            'purchase': False,
            'review': 'Just browsing, but the team was very helpful and knowledgeable.',
            'purchase_date': '2024-04-05',
            'car_make': 'Nissan',
            'car_model': 'Altima',
            'car_year': 2024,
            'sentiment': 'positive'
        },
        {
            'id': 5,
            'dealership': 4,
            'name': 'Robert Brown',
            'purchase': True,
            'review': 'Top-notch luxury vehicles and exceptional service!',
            'purchase_date': '2024-01-25',
            'car_make': 'Porsche',
            'car_model': '911',
            'car_year': 2024,
            'sentiment': 'positive'
        },
        {
            'id': 6,
            'dealership': 5,
            'name': 'Lisa Garcia',
            'purchase': True,
            'review': 'Perfect SUV for desert driving. Great deals!',
            'purchase_date': '2024-02-14',
            'car_make': 'Jeep',
            'car_model': 'Wrangler',
            'car_year': 2023,
            'sentiment': 'positive'
        },
    ])
    
    print(f"Sample data initialized successfully!")
    print(f"Dealers: {len(dealers_data)}")
    print(f"Reviews: {len(reviews_data)}")
