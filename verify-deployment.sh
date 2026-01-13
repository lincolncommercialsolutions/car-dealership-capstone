#!/bin/bash

echo "=========================================="
echo "Car Dealership Deployment Verification"
echo "=========================================="
echo ""

# Get public IP
PUBLIC_IP=$(curl -s ifconfig.me)
echo "✓ Public IP: $PUBLIC_IP"
echo ""

# Check if containers are running
echo "Checking Docker containers..."
docker compose ps
echo ""

# Test services locally
echo "Testing services locally..."
echo ""

echo "1. Testing Django (port 8000)..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/static/Home.html)
if [ "$HTTP_CODE" = "200" ]; then
    echo "   ✓ Django is working locally"
else
    echo "   ✗ Django returned HTTP $HTTP_CODE"
    echo "   Check logs: docker compose logs django --tail=50"
fi
echo ""

echo "2. Testing Sentiment Analyzer (port 5000)..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5000/analyze/test)
if [ "$HTTP_CODE" = "200" ]; then
    echo "   ✓ Sentiment Analyzer is working locally"
else
    echo "   ✗ Sentiment Analyzer returned HTTP $HTTP_CODE"
fi
echo ""

echo "3. Testing Car Inventory (port 5001)..."
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:5001/carmakes)
if [ "$HTTP_CODE" = "200" ]; then
    echo "   ✓ Car Inventory is working locally"
else
    echo "   ✗ Car Inventory returned HTTP $HTTP_CODE"
fi
echo ""

echo "=========================================="
echo "If all services work locally but NOT from browser:"
echo "=========================================="
echo ""
echo "YOU NEED TO CONFIGURE AWS SECURITY GROUP:"
echo ""
echo "1. Go to AWS Console → EC2 → Instances"
echo "2. Click your instance → Security tab"
echo "3. Click the security group link"
echo "4. Edit Inbound Rules → Add Rules:"
echo "   - Type: Custom TCP, Port: 8000, Source: 0.0.0.0/0"
echo "   - Type: Custom TCP, Port: 5000, Source: 0.0.0.0/0"
echo "   - Type: Custom TCP, Port: 5001, Source: 0.0.0.0/0"
echo "5. Save rules"
echo ""
echo "=========================================="
echo "Your application URLs:"
echo "=========================================="
echo ""
echo "http://$PUBLIC_IP:8000/static/Home.html"
echo "http://$PUBLIC_IP:8000/static/Dealerships.html"
echo "http://$PUBLIC_IP:8000/djangoapp/about"
echo ""
echo "=========================================="
