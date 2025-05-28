from flask import Flask, request, jsonify
from app import translate_text

app = Flask(__name__)

@app.route("/translate", methods=["POST"])
def translate():
    json_data = request.json
    if not json_data:
        return jsonify({"error": "JSON body missing"}), 400

    text = json_data.get("text")
    to = json_data.get("to")
    if not text or not to:
        return jsonify({"error": "'text' and 'to' parameters required"}), 400

    result = translate_text(text, to)
    return jsonify(result)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
