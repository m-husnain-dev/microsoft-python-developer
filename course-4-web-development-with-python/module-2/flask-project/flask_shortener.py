from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
import string
import random
from datetime import datetime
from collections import defaultdict

app = Flask(__name__)
CORS(app)

# In-memory storage (use database for production)
urls_db = {}  # short_code -> { original_url, created_at, clicks, referrers }
analytics_db = defaultdict(lambda: {'clicks': 0, 'referrers': []})

def generate_short_code(length=6):
    """Generate random short code"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    """Create shortened URL"""
    data = request.json
    original_url = data.get('url')
    
    if not original_url:
        return jsonify({'error': 'URL required'}), 400
    
    # Validate URL
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'https://' + original_url
    
    short_code = generate_short_code()
    
    # Avoid collisions
    while short_code in urls_db:
        short_code = generate_short_code()
    
    urls_db[short_code] = {
        'original_url': original_url,
        'created_at': datetime.now().isoformat(),
        'clicks': 0
    }
    
    short_url = f"http://localhost:5000/{short_code}"
    return jsonify({'short_url': short_url, 'code': short_code}), 201

@app.route('/<short_code>')
def redirect_to_url(short_code):
    """Redirect to original URL and track analytics"""
    if short_code not in urls_db:
        return jsonify({'error': 'Not found'}), 404
    
    # Track click
    urls_db[short_code]['clicks'] += 1
    referrer = request.referrer or 'direct'
    
    if 'referrers' not in urls_db[short_code]:
        urls_db[short_code]['referrers'] = []
    
    urls_db[short_code]['referrers'].append({
        'referrer': referrer,
        'timestamp': datetime.now().isoformat()
    })
    
    return redirect(urls_db[short_code]['original_url'])

@app.route('/api/stats/<short_code>')
def get_stats(short_code):
    """Get analytics for shortened URL"""
    if short_code not in urls_db:
        return jsonify({'error': 'Not found'}), 404
    
    url_data = urls_db[short_code]
    
    return jsonify({
        'short_code': short_code,
        'original_url': url_data['original_url'],
        'created_at': url_data['created_at'],
        'total_clicks': url_data['clicks'],
        'referrers': url_data.get('referrers', [])
    })

@app.route('/api/urls')
def list_urls():
    """List all shortened URLs (for testing)"""
    result = []
    for code, data in urls_db.items():
        result.append({
            'code': code,
            'original': data['original_url'],
            'clicks': data['clicks'],
            'created': data['created_at']
        })
    return jsonify(result)

@app.route('/health')
def health():
    """Health check"""
    return jsonify({'status': 'alive'})

if __name__ == '__main__':
    print("🚀 Flask URL Shortener running on http://localhost:5000")
    print("\nAPI Endpoints:")
    print("POST /api/shorten - Create short URL")
    print("GET /<code> - Redirect to original")
    print("GET /api/stats/<code> - View analytics")
    print("GET /api/urls - List all URLs")
    
    app.run(debug=True, port=5000)
