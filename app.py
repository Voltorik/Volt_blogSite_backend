from flask import Flask, Response, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/api/substack', methods=['GET'])

def proxy_substack_feed():
    url = "https://voltorik.substack.com/feed"

    try:
        # test network connection
        res = requests.get(url, timeout=5)
        res.raise_for_status() # raises error is not a 200 status

        # Return the raw XML with proper content-type
        return Response(res.content, mimetype='application/xml')
    except requests.exceptions.RequestException as e:
        return jsonify({"Error": "Failed to fetch RSS feed", "details":str(e)}), 502
    except Exception as e:
        return jsonify({"Error": "Internal server error", "details":str(e)}), 500

if __name__ == "__main__":
    PORT = int(os.environ.get("PORT", 5000)) # deafult to 5000 for local dev
    app.run(host="0.0.0.0", port=PORT, debug=False)