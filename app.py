import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Hello Cloud!</h1>
    <p>Nama: Irman</p>
    <p>Universitas Djuanda Bogor - Komputasi Awan</p>
    <p>Versi 1</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
