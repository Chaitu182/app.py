from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Define a list of URLs to ping
urls_to_check = [
    "http://devopsenginer.com",
    "http://devopsenginer.org",
    "http://devopsenginer.net"
]

@app.route('/check_urls', methods=['GET'])
def check_urls():
    results = {}
    for url in urls_to_check:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results[url] = True
            else:
                results[url] = False
        except requests.exceptions.RequestException as e:
            results[url] = False
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
