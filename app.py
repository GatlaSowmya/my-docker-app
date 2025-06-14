from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    version = os.getenv('APP_VERSION', 'Unknown')
    return f"✅ Welcome visys cloud technologies!{version}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



