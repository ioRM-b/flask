from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Ramos Morlet Iovanni", "+524756987", "Josue Perez", "+456789123"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
