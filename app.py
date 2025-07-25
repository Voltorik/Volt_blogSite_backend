from flask import Flask, Response, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)
localPort = int(5000)

@app.route('/api/substack', methods=['GET'])

def proxy_substack_feed():
    url = "https://voltorik.substack.com/feed"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() # raises error is not a 200 status

        return Response(response.content, mimetype='application/xml')
    except requests.exceptions.RequestException as e:
        return jsonify({"Error": "Failed to fetch RSS feed", "details":str(e)}), 502
    except Exception as e:
        return jsonify({"Error": "Internal server error", "details":str(e)}), 500

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", localPort)) 
    app.run(host="0.0.0.0", port=PORT, debug=False)