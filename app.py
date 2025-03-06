from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Irene <3! Your Flask app is live on Render."

@app.route('/run-script')
def run_script():
    result = sum(range(1, 101))  # Example script: Sum of 1 to 100
    return f"Script executed! The result is: {result}"

if __name__ == '__main__':
    app.run()
