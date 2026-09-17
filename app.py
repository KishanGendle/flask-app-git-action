from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Runs on port 5000 by default
    app.run(host="0.0.0.0", port=5000)
    