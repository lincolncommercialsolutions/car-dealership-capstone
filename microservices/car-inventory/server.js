const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 5001;

// Middleware
app.use(cors());
app.use(express.json());

// Sample car data
const cars = [
    {
        id: 1,
        make: 'Toyota',
        models: ['Camry', 'Corolla', 'RAV4', 'Highlander', 'Tacoma'],
        description: 'Reliable and fuel-efficient vehicles'
    },
    {
        id: 2,
        make: 'Honda',
        models: ['Accord', 'Civic', 'CR-V', 'Pilot', 'Odyssey'],
        description: 'Quality engineering and performance'
    },
    {
        id: 3,
        make: 'Ford',
        models: ['F-150', 'Mustang', 'Explorer', 'Escape', 'Edge'],
        description: 'American-made tough and reliable'
    },
    {
        id: 4,
        make: 'Chevrolet',
        models: ['Silverado', 'Malibu', 'Equinox', 'Traverse', 'Tahoe'],
        description: 'Performance and durability'
    },
    {
        id: 5,
        make: 'BMW',
        models: ['3 Series', '5 Series', 'X3', 'X5', 'M3'],
        description: 'Luxury and performance combined'
    },
    {
        id: 6,
        make: 'Mercedes-Benz',
        models: ['C-Class', 'E-Class', 'GLE', 'GLC', 'S-Class'],
        description: 'Elegance and innovation'
    },
    {
        id: 7,
        make: 'Nissan',
        models: ['Altima', 'Sentra', 'Rogue', 'Pathfinder', 'Frontier'],
        description: 'Innovation that excites'
    },
    {
        id: 8,
        make: 'Hyundai',
        models: ['Elantra', 'Sonata', 'Tucson', 'Santa Fe', 'Palisade'],
        description: 'Modern design and technology'
    }
];

// Routes
app.get('/get_cars', (req, res) => {
    res.json(cars);
});

app.get('/get_cars/:make', (req, res) => {
    const make = req.params.make;
    const car = cars.find(c => c.make.toLowerCase() === make.toLowerCase());
    
    if (car) {
        res.json(car);
    } else {
        res.status(404).json({ error: 'Car make not found' });
    }
});

app.get('/health', (req, res) => {
    res.json({ status: 'healthy', service: 'car-inventory' });
});

// Start server
app.listen(PORT, () => {
    console.log(`Car Inventory Service running on port ${PORT}`);
});

module.exports = app;
