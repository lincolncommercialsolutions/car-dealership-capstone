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
        {
            'id': 9,
            'name': 'Empire Auto Sales',
            'city': 'New York',
            'state': 'New York',
            'address': '555 Broadway',
            'zip': '10012',
            'lat': 40.7128,
            'long': -74.0060,
            'cars': ['Cadillac Escalade', 'Lincoln Navigator', 'GMC Yukon', 'Infiniti QX80']
        },
        {
            'id': 10,
            'name': 'Gateway Motors',
            'city': 'St. Louis',
            'state': 'Missouri',
            'address': '321 Gateway Dr',
            'zip': '63101',
            'lat': 38.6270,
            'long': -90.1994,
            'cars': ['Chevrolet Tahoe', 'Ford Explorer', 'Nissan Pathfinder', 'Volkswagen Atlas']
        },
        {
            'id': 11,
            'name': 'Emerald City Auto',
            'city': 'Seattle',
            'state': 'Washington',
            'address': '777 Pike St',
            'zip': '98101',
            'lat': 47.6062,
            'long': -122.3321,
            'cars': ['Volvo XC90', 'Acura MDX', 'Genesis GV80', 'Alfa Romeo Stelvio']
        },
        {
            'id': 12,
            'name': 'Lone Star Automotive',
            'city': 'Houston',
            'state': 'Texas',
            'address': '999 Texas Ave',
            'zip': '77002',
            'lat': 29.7604,
            'long': -95.3698,
            'cars': ['Ford F-250', 'Chevrolet Colorado', 'Toyota Tundra', 'GMC Sierra']
        },
        {
            'id': 13,
            'name': 'Peachtree Auto Group',
            'city': 'Atlanta',
            'state': 'Georgia',
            'address': '150 Peachtree St',
            'zip': '30303',
            'lat': 33.7490,
            'long': -84.3880,
            'cars': ['Kia Telluride', 'Hyundai Palisade', 'Mitsubishi Outlander', 'Buick Enclave']
        },
        {
            'id': 14,
            'name': 'Motor City Classics',
            'city': 'Detroit',
            'state': 'Michigan',
            'address': '888 Woodward Ave',
            'zip': '48226',
            'lat': 42.3314,
            'long': -83.0458,
            'cars': ['Dodge Durango', 'Chrysler 300', 'Jeep Grand Cherokee', 'Ram 2500']
        },
        {
            'id': 15,
            'name': 'Liberty Auto Exchange',
            'city': 'Philadelphia',
            'state': 'Pennsylvania',
            'address': '444 Market St',
            'zip': '19106',
            'lat': 39.9526,
            'long': -75.1652,
            'cars': ['Toyota Highlander', 'Honda Pilot', 'Mazda CX-90', 'Nissan Armada']
        },
        {
            'id': 16,
            'name': 'Windy City Wheels',
            'city': 'Chicago',
            'state': 'Illinois',
            'address': '200 State St',
            'zip': '60601',
            'lat': 41.8781,
            'long': -87.6298,
            'cars': ['Audi Q7', 'BMW X5', 'Mercedes-Benz GLE', 'Porsche Cayenne']
        },
        {
            'id': 17,
            'name': 'Boston Bay Motors',
            'city': 'Boston',
            'state': 'Massachusetts',
            'address': '600 Atlantic Ave',
            'zip': '02210',
            'lat': 42.3601,
            'long': -71.0589,
            'cars': ['Volvo S60', 'Lexus ES', 'Acura TLX', 'Genesis G80']
        },
        {
            'id': 18,
            'name': 'Desert Oasis Auto',
            'city': 'Las Vegas',
            'state': 'Nevada',
            'address': '777 Las Vegas Blvd',
            'zip': '89101',
            'lat': 36.1699,
            'long': -115.1398,
            'cars': ['Maserati Ghibli', 'Bentley Continental', 'Aston Martin Vantage', 'McLaren GT']
        },
        {
            'id': 19,
            'name': 'Pacific Northwest Auto',
            'city': 'Portland',
            'state': 'Oregon',
            'address': '888 SW Broadway',
            'zip': '97205',
            'lat': 45.5152,
            'long': -122.6784,
            'cars': ['Subaru Crosstrek', 'Toyota RAV4', 'Honda HR-V', 'Mazda CX-30']
        },
        {
            'id': 20,
            'name': 'Mile High Auto Gallery',
            'city': 'Colorado Springs',
            'state': 'Colorado',
            'address': '1500 S Nevada Ave',
            'zip': '80903',
            'lat': 38.8339,
            'long': -104.8214,
            'cars': ['Ford Bronco', 'Chevrolet Blazer', 'Jeep Gladiator', 'Toyota Tacoma']
        },
        {
            'id': 21,
            'name': 'Sunshine State Motors',
            'city': 'Tampa',
            'state': 'Florida',
            'address': '300 Tampa St',
            'zip': '33602',
            'lat': 27.9506,
            'long': -82.4572,
            'cars': ['Volkswagen Jetta', 'Kia Forte', 'Hyundai Elantra', 'Honda Civic']
        },
        {
            'id': 22,
            'name': 'Golden Gate Auto',
            'city': 'San Francisco',
            'state': 'California',
            'address': '100 Market St',
            'zip': '94105',
            'lat': 37.7749,
            'long': -122.4194,
            'cars': ['BMW i4', 'Audi e-tron', 'Jaguar I-PACE', 'Mercedes-Benz EQS']
        },
        {
            'id': 23,
            'name': 'Music City Motors',
            'city': 'Nashville',
            'state': 'Tennessee',
            'address': '400 Broadway',
            'zip': '37203',
            'lat': 36.1627,
            'long': -86.7816,
            'cars': ['GMC Acadia', 'Buick Encore', 'Cadillac XT5', 'Chevrolet Traverse']
        },
        {
            'id': 24,
            'name': 'Twin Cities Auto',
            'city': 'Minneapolis',
            'state': 'Minnesota',
            'address': '250 Nicollet Mall',
            'zip': '55401',
            'lat': 44.9778,
            'long': -93.2650,
            'cars': ['Subaru Legacy', 'Volkswagen Passat', 'Toyota Avalon', 'Honda Accord Hybrid']
        },
        {
            'id': 25,
            'name': 'Queen City Automotive',
            'city': 'Charlotte',
            'state': 'North Carolina',
            'address': '500 Tryon St',
            'zip': '28202',
            'lat': 35.2271,
            'long': -80.8431,
            'cars': ['Ford Edge', 'Chevrolet Equinox', 'Nissan Rogue', 'Hyundai Tucson']
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
