#!/bin/bash

# MongoDB initialization script for Car Dealership database

echo "Initializing Car Dealership MongoDB database..."

# Connect to MongoDB and initialize data
mongosh <<EOF

use dealerships;

// Clear existing data
db.dealers.deleteMany({});
db.reviews.deleteMany({});

// Insert sample dealers
db.dealers.insertMany([
    {
        id: 1,
        name: "Premium Motors",
        city: "Kansas City",
        state: "Kansas",
        address: "123 Main St",
        zip: "66101",
        lat: 39.0997,
        long: -94.5786,
        short_name: "premium",
        full_name: "Premium Motors Kansas City"
    },
    {
        id: 2,
        name: "AutoHub Central",
        city: "Topeka",
        state: "Kansas",
        address: "456 Oak Ave",
        zip: "66603",
        lat: 39.0558,
        long: -95.6890,
        short_name: "autohub",
        full_name: "AutoHub Central Topeka"
    },
    {
        id: 15,
        name: "Elite Car Sales",
        city: "Wichita",
        state: "Kansas",
        address: "789 Elm St",
        zip: "67202",
        lat: 37.6872,
        long: -97.3301,
        short_name: "elite",
        full_name: "Elite Car Sales Wichita"
    },
    {
        id: 16,
        name: "Sunshine Auto Group",
        city: "Overland Park",
        state: "Kansas",
        address: "321 Park Blvd",
        zip: "66204",
        lat: 38.9822,
        long: -94.6708,
        short_name: "sunshine",
        full_name: "Sunshine Auto Group Overland Park"
    },
    {
        id: 17,
        name: "Metro Car Center",
        city: "Austin",
        state: "Texas",
        address: "555 Congress Ave",
        zip: "78701",
        lat: 30.2672,
        long: -97.7431,
        short_name: "metro",
        full_name: "Metro Car Center Austin"
    }
]);

// Insert sample reviews
db.reviews.insertMany([
    {
        id: 1,
        dealership: 15,
        name: "John Smith",
        purchase: true,
        review: "Fantastic services and great customer support!",
        purchase_date: "2024-01-15",
        car_make: "Toyota",
        car_model: "Camry",
        car_year: 2023,
        sentiment: "positive"
    },
    {
        id: 2,
        dealership: 15,
        name: "Jane Doe",
        purchase: true,
        review: "Excellent experience, highly recommend this dealership.",
        purchase_date: "2024-02-20",
        car_make: "Honda",
        car_model: "Accord",
        car_year: 2023,
        sentiment: "positive"
    },
    {
        id: 3,
        dealership: 1,
        name: "Mike Johnson",
        purchase: true,
        review: "Professional staff and smooth transaction process.",
        purchase_date: "2024-03-10",
        car_make: "Ford",
        car_model: "F-150",
        car_year: 2024,
        sentiment: "positive"
    },
    {
        id: 4,
        dealership: 2,
        name: "Sarah Williams",
        purchase: false,
        review: "Good selection of vehicles, friendly salespeople.",
        purchase_date: null,
        car_make: null,
        car_model: null,
        car_year: null,
        sentiment: "positive"
    }
]);

print("Database initialized successfully!");
print("Dealers inserted: " + db.dealers.countDocuments());
print("Reviews inserted: " + db.reviews.countDocuments());

EOF

echo "MongoDB initialization complete!"
