from flask import Flask
import os

app = Flask(__name__)
version = os.environ.get("APP_VERSION", "v0")

@app.route("/")
def home():
    return f"✅ Welcome visys cloud technologies-1! - {version}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
