import requests
import json

BASE_URL = "http://localhost:5000"

def test_shortener():
    print("🧪 Testing Flask URL Shortener\n")
    
    # Test 1: Create shortened URL
    print("1️⃣ Creating shortened URL...")
    response = requests.post(f"{BASE_URL}/api/shorten", json={
        'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
    })
    print(f"Status: {response.status_code}")
    data = response.json()
    print(f"Response: {json.dumps(data, indent=2)}\n")
    
    short_code = data['code']
    
    # Test 2: List all URLs
    print("2️⃣ Listing all shortened URLs...")
    response = requests.get(f"{BASE_URL}/api/urls")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")
    
    # Test 3: Get stats before redirect
    print("3️⃣ Getting stats (before redirect)...")
    response = requests.get(f"{BASE_URL}/api/stats/{short_code}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")
    
    # Test 4: Simulate redirect (track click)
    print("4️⃣ Simulating redirect (tracks click)...")
    response = requests.get(f"{BASE_URL}/{short_code}", allow_redirects=False)
    print(f"Status: {response.status_code}")
    print(f"Redirects to: {response.headers.get('Location')}\n")
    
    # Test 5: Get stats after redirect
    print("5️⃣ Getting stats (after redirect)...")
    response = requests.get(f"{BASE_URL}/api/stats/{short_code}")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")
    
    # Test 6: Health check
    print("6️⃣ Health check...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}\n")

if __name__ == '__main__':
    try:
        test_shortener()
    except ConnectionError:
        print("❌ Connection failed. Is Flask server running?")
        print("Run: python flask_shortener.py")
