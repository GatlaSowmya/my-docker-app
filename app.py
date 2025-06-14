from flask import Flask, request
import os

app = Flask(__name__)
DATA_FILE = "/data/store.txt"
VERSION = os.getenv("APP_VERSION", "Unknown")

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        message = request.form.get("message", "")
        with open(DATA_FILE, "a") as f:
            f.write(f"{message}\n")
        return f"✅ Message saved in container {VERSION}"

    elif request.method == 'GET':
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE) as f:
                content = f.read()
        else:
            content = "No data yet"
        return f"<h3>Container {VERSION} Data:</h3><pre>{content}</pre>" + """
            <form method="POST">
                <input name="message" placeholder="Enter message" />
                <input type="submit" />
            </form>
        """

if __name__ == '__main__':
    os.makedirs("/data", exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
