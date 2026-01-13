# 🚀 Premium Auto Gallery - AWS Deployment Checklist

## ✅ Pre-Deployment Tasks (COMPLETED)

- [x] UI/UX complete overhaul with professional design
- [x] All static pages redesigned (Home, About, Contact)
- [x] Modern luxury car dealership theme implemented
- [x] High-quality background images integrated
- [x] Responsive design for all devices
- [x] All code committed and pushed to GitHub
- [x] CI/CD pipeline configured and tested
- [x] Documentation complete (final-answers-and-responses.txt)
- [x] Screenshot guide prepared with all URLs
- [x] Peer reviewer message drafted

## 📦 What's Ready for AWS

### Application Components
- ✅ Django backend (port 8000)
- ✅ MongoDB database (port 27017)
- ✅ Sentiment Analyzer microservice (port 5000)
- ✅ Car Inventory microservice (port 5001)
- ✅ Docker & Docker Compose configuration
- ✅ Kubernetes manifests (optional)

### Files to Deploy
```
Car-Dealership/
├── docker-compose.yml (main orchestration)
├── Dockerfile (Django app)
├── server/ (Django project)
├── microservices/ (Flask + Node.js services)
├── kubernetes/ (K8s configs - optional)
└── .github/workflows/ (CI/CD)
```

## 🌐 AWS EC2 Deployment Steps

### 1. Launch EC2 Instance
```bash
# Recommended: Ubuntu 22.04 LTS
# Instance Type: t2.medium or larger
# Storage: 20GB minimum
# Security Group: Open ports 22, 80, 8000, 5000, 5001, 27017
```

### 2. Connect to EC2
```bash
ssh -i your-key.pem ubuntu@[EC2-PUBLIC-IP]
```

### 3. Install Docker
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify
docker --version
docker-compose --version
```

### 4. Clone Repository
```bash
git clone https://github.com/lincolncommercialsolutions/car-dealership-capstone.git
cd car-dealership-capstone
```

### 5. Configure for Production
```bash
# Update Django settings for production
# Edit server/dealership/settings.py:
# - Set DEBUG = False
# - Update ALLOWED_HOSTS = ['[EC2-PUBLIC-IP]', 'localhost']
# - Configure STATIC_ROOT (already done)
```

### 6. Launch Application
```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

### 7. Initialize Database
```bash
# Create superuser
docker-compose exec django python manage.py createsuperuser

# Verify services
curl http://localhost:8000/djangoapp/get_dealers
curl http://localhost:5000/analyze/review -X POST -H "Content-Type: application/json" -d '{"text":"test"}'
curl http://localhost:5001/get_cars
```

### 8. Configure AWS Security Group
Open the following ports:
- Port 22: SSH (your IP only)
- Port 80: HTTP (0.0.0.0/0)
- Port 8000: Django (0.0.0.0/0)
- Port 5000: Sentiment service (0.0.0.0/0)
- Port 5001: Car inventory (0.0.0.0/0)
- Port 27017: MongoDB (127.0.0.1 only - security)

### 9. Test Deployment
```bash
# Replace [EC2-PUBLIC-IP] with actual IP

# Test Django
curl http://[EC2-PUBLIC-IP]:8000/djangoapp/get_dealers

# Test frontend
curl http://[EC2-PUBLIC-IP]:8000/static/Home.html

# Test microservices
curl http://[EC2-PUBLIC-IP]:5000/analyze/review -X POST -H "Content-Type: application/json" -d '{"text":"great car"}'
curl http://[EC2-PUBLIC-IP]:5001/get_cars
```

## 📸 Screenshot Checklist (28 Tasks)

After deployment, capture these screenshots:

### Static Pages (Tasks 2-4)
- [ ] Django server running (terminal/logs)
- [ ] About Us page
- [ ] Contact Us page

### User Management (Tasks 5-7)
- [ ] Home page - logged in
- [ ] Logout alert
- [ ] Sign-up page

### API Endpoints (Tasks 8-11)
- [ ] Dealer reviews
- [ ] All dealerships
- [ ] Dealer details
- [ ] Kansas dealers

### Admin Panel (Tasks 12-15)
- [ ] Admin login
- [ ] Admin logout
- [ ] Car makes API
- [ ] Car models in admin

### Microservices (Task 16)
- [ ] Sentiment analyzer response

### Dynamic Pages (Tasks 17-22)
- [ ] Dealers before login
- [ ] Dealers after login
- [ ] Dealers filtered by state
- [ ] Dealer details with reviews
- [ ] Review form filled
- [ ] Posted review displayed

### CI/CD (Task 23)
- [ ] GitHub Actions success

### Deployed App (Tasks 25-28)
- [ ] Deployed landing page
- [ ] Deployed logged-in state
- [ ] Deployed dealer details
- [ ] Deployed review submission

## 🔧 Troubleshooting

### Container won't start
```bash
docker-compose logs [service-name]
docker-compose down
docker-compose up -d --build
```

### Port already in use
```bash
sudo lsof -i :[port]
sudo kill -9 [PID]
```

### MongoDB connection issues
```bash
docker-compose exec mongodb mongosh
# Check if DB is accessible
```

### Static files not loading
```bash
docker-compose exec django python manage.py collectstatic --noinput
```

## 📝 Update Deployment URL

After AWS deployment, update these files:
1. `final-answers-and-responses.txt` - Replace localhost with EC2 IP
2. `deploymentURL.txt` - Add actual deployment URL
3. Take all screenshots using EC2 public IP

## ✨ Post-Deployment

- [ ] All services running and accessible
- [ ] Admin user created
- [ ] Test data populated
- [ ] All 28 screenshots captured
- [ ] URLs updated in submission document
- [ ] Peer review message finalized
- [ ] Ready to submit!

---

## 🎯 Final Submission Files

1. GitHub Repository URL
2. Deployment URL (EC2 public IP:8000)
3. 27 screenshot files (properly named)
4. final-answers-and-responses.txt

Good luck with your submission! 🚗✨
