from flask import Flask, request, jsonify
from flask_cors import CORS
from compare import compare_all
import os
print("Working dir:", os.getcwd())
print("Contents:", os.listdir())


app = Flask(__name__)
CORS(app)

@app.route("/compare", methods=["POST"])
def compare():
    data = request.get_json()
    product_name = data.get("product_name")
    result = compare_all(product_name)
    return jsonify(result)

if __name__ == "__main__":
    app.run()
