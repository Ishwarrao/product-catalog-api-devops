import requests

products = [
    {"name": "Wireless Headphones", "price": 99.99, "description": "High quality over-ear wireless headphones."},
    {"name": "Smartphone", "price": 699.99, "description": "Latest model smartphone with OLED display."},
    {"name": "Gaming Laptop", "price": 1299.99, "description": "Powerful laptop with RTX GPU for gaming."},
    {"name": "Bluetooth Speaker", "price": 49.99, "description": "Portable speaker with deep bass."},
    {"name": "Smartwatch", "price": 199.99, "description": "Fitness tracking smartwatch with heart rate monitor."},
    {"name": "Digital Camera", "price": 499.99, "description": "24MP mirrorless camera with 4K video."},
    {"name": "Electric Toothbrush", "price": 79.99, "description": "Rechargeable toothbrush with multiple modes."},
    {"name": "Coffee Maker", "price": 89.99, "description": "Automatic coffee maker with programmable timer."},
    {"name": "Gaming Chair", "price": 299.99, "description": "Ergonomic chair built for extended gaming."},
    {"name": "4K Monitor", "price": 349.99, "description": "27-inch UHD monitor with HDR support."},
    {"name": "Wireless Mouse", "price": 29.99, "description": "Ergonomic mouse with customizable buttons."},
    {"name": "Mechanical Keyboard", "price": 109.99, "description": "RGB backlit mechanical keyboard with blue switches."},
    {"name": "External SSD", "price": 159.99, "description": "Portable 1TB solid-state drive with USB-C."},
    {"name": "Noise Cancelling Earbuds", "price": 129.99, "description": "Compact earbuds with active noise cancellation."},
    {"name": "Fitness Tracker", "price": 89.99, "description": "Waterproof tracker with sleep monitoring."},
    {"name": "Smart Thermostat", "price": 249.99, "description": "Wi-Fi thermostat with remote control."},
    {"name": "Drone", "price": 399.99, "description": "Quadcopter drone with HD camera."},
    {"name": "Electric Scooter", "price": 499.99, "description": "Foldable electric scooter with 20-mile range."},
    {"name": "Action Camera", "price": 199.99, "description": "Compact action camera with waterproof case."},
    {"name": "Smart Light Bulbs", "price": 59.99, "description": "Set of 4 color-changing LED bulbs."}
]

url = 'http://127.0.0.1:5000/products'

for product in products:
    response = requests.post(url, json=product)
    if response.status_code == 201:
        print(f"Added: {product['name']}")
    else:
        print(f"Failed to add: {product['name']} - {response.text}")