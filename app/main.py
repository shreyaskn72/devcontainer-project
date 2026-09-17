from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "API is running", "endpoint": "/api/hello"})

@app.route('/api/hello', methods=['GET'])
def hello_world():
    # jsonify automatically format the dictionary as a JSON response
    return jsonify({"message": "Hello from Shreyas"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
