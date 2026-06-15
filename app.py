from flask import Flask, jsonify
import json

app = Flask(__name__)

# ---------- Load Config ----------
def load_config():

    with open(
        "config.json",
        "r"
    ) as file:

        return json.load(file)

# ---------- Get All Config ----------
@app.route("/config")
def get_config():

    return jsonify(
        load_config()
    )

# ---------- Get Single Config ----------
@app.route(
    "/config/<key>"
)
def get_config_key(key):

    config = load_config()

    if key not in config:

        return jsonify({
            "message":
            "Key not found"
        }), 404

    return jsonify({
        key: config[key]
    })

# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status": "healthy"
    })

# ---------- Run ----------
if __name__ == "__main__":

    app.run(
        port=5000,
        debug=True
    )
