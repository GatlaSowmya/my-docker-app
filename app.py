from flask import Flask, request
import os

app = Flask(__name__)

VERSION = os.environ.get("APP_VERSION", "1")
DATA_FILE = "/data/data.txt"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.form.get('message', '')
        with open(DATA_FILE, 'a') as f:
            f.write(f"{msg}\n")
        return f"✅ Data saved in Container {VERSION}"

    elif request.method == 'GET':
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE) as f:
                content = f.read()
        else:
            content = "No data yet."

        label = "Old" if VERSION == "1" else "New"
        return f"""
        <h2>Container {VERSION} ({label}) Data:</h2>
        <pre>{content}</pre>
        <form method='POST'>
            <input name='message' placeholder='Enter message' />
            <button type='submit'>Submit</button>
        </form>
        """
        
if __name__ == '__main__':
    os.makedirs('/data', exist_ok=True)
    app.run(host='0.0.0.0', port=5000)
