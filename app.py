from flask import Flask, jsonify
import feedparser
import requests

app = Flask(__name__)
@app.route("/api/substack")

def getSubstackFeed():
    feedURL = "https://voltorik.substack.com/feed"

    try:
        # test network connection
        res = requests.get(feedURL, timeout=5)
        res.raise_for_status() # raises error is not a 200 status
        feed = feedparser.parse(feedURL)

        if not feed.entries:
            return jsonify({"Error": "No articles found in feed"}), 404
        
        articles = [
            {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "summary": entry.summary
            }
            for entry in feed.entries
        ]
        return jsonify(articles)
    except requests.exceptions.RequestException as e:
        return jsonify({"Error": "Failed to fetch RSS feed", "details":str(e)}), 502
    except Exception as e:
        return jsonify({"Error": "Internal server error", "details":str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)