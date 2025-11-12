from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World App</title>
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                text-align: center;
                background: linear-gradient(135deg, #89f7fe, #66a6ff);
                color: #333;
                margin-top: 100px;
            }
            h1 {
                font-size: 3em;
                color: white;
                text-shadow: 2px 2px 4px #000000;
            }
            p {
                font-size: 1.2em;
                color: #f0f0f0;
            }
            button {
                margin-top: 20px;
                padding: 10px 20px;
                background-color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
            }
            button:hover {
                background-color: #ddd;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World! 🌎</h1>
        <p>Welcome to my Flask app deployed on Render.</p>
        <button onclick="alert('This app works perfectly!')">Click Me</button>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
