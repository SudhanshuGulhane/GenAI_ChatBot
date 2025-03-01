from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from src.query_processing import process_query

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/get", methods=["GET", "POST"])
def chatbot():  
    input = request.form["msg"]
    response = process_query(input)
    return str(response["answer"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)