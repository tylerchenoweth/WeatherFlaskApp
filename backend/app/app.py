from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Restrict CORS to React frontend only
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

import routes

if __name__ == '__main__':
    app.run(port=5000, debug=True)