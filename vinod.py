from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/fetch', methods=['GET'])
def fetch_data():
    url = "https://jsonplaceholder.typicode.com/todos/1"  # Example API
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()  
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
