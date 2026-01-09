# Car Dealership Capstone Project

Full-stack web application for a car dealership with dealer listings, reviews, and sentiment analysis.

## Tech Stack

- **Frontend**: React.js with React Router
- **Backend**: Django REST Framework
- **Microservices**: Flask (Sentiment Analysis), Node.js (Car Inventory)
- **Databases**: SQLite (dealers/users), MongoDB (reviews)
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions
- **Deployment**: IBM Cloud Code Engine

## Features

- User authentication (login, logout, register)
- Browse car dealerships by location/state
- View dealer details and customer reviews
- Post reviews with sentiment analysis
- Responsive UI with static pages (About, Contact)
- Admin panel for data management

## Project Structure

```
car-dealership-capstone/
├── server/
│   ├── djangoapp/          # Django REST API
│   ├── database/           # Database configs
│   └── frontend/           # React application
├── microservices/
│   ├── sentiment-analyzer/ # Flask sentiment service
│   └── car-inventory/      # Node.js car data service
├── kubernetes/             # K8s deployment manifests
├── .github/workflows/      # CI/CD pipelines
└── README.md
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- Node.js 16+
- MongoDB
- Docker Desktop
- IBM Cloud CLI

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/car-dealership-capstone.git
   cd car-dealership-capstone
   ```

2. **Set up Django backend**
   ```bash
   cd server
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
   ```

3. **Set up React frontend**
   ```bash
   cd server/frontend
   npm install
   npm start
   ```

4. **Run microservices**
   ```bash
   # Sentiment analyzer
   cd microservices/sentiment-analyzer
   python app.py
   
   # Car inventory
   cd microservices/car-inventory
   node server.js
   ```

### Docker Deployment

```bash
docker-compose up --build
```

### Kubernetes Deployment

```bash
kubectl apply -f kubernetes/
```

## API Endpoints

### Authentication
- `POST /djangoapp/login` - User login
- `GET /djangoapp/logout` - User logout
- `POST /djangoapp/register` - User registration

### Dealers
- `GET /djangoapp/get_dealers` - Get all dealers
- `GET /djangoapp/get_dealers/<id>` - Get dealer by ID
- `GET /djangoapp/get_dealers?state=<state>` - Filter dealers by state

### Reviews
- `GET /djangoapp/get_reviews?dealerId=<id>` - Get reviews for dealer
- `POST /djangoapp/add_review` - Submit new review

### Microservices
- `GET /get_cars` - Get all car makes/models (port 5001)
- `POST /analyze/<text>` - Sentiment analysis (port 5000)

## Testing

Run Django tests:
```bash
cd server
python manage.py test
```

Run frontend tests:
```bash
cd server/frontend
npm test
```

## Deployment URL

[Insert your IBM Cloud Code Engine URL here]

## Contributors

- [Your Name] - Full Stack Developer

## License

This project is part of an IBM Full Stack Development Capstone.

## Acknowledgments

- IBM Skills Network
- Course Instructors
