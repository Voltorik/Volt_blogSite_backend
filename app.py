from flask import Flask, Response
import requests

app = Flask(__name__)

@app.route('/api/substack', methods=['GET'])
def proxy_substack_feed():
    url = 'https://voltorik.substack.com/feed'
    r = requests.get(url)
    
    # Return the raw XML with proper content-type
    return Response(r.content, mimetype='application/xml')