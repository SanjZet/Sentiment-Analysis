from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """<!DOCTYPE html>
<html>
<head>
    <title>Flask Test</title>
</head>
<body>
    <h1>✅ Flask is working!</h1>
    <p>If you see this, the issue was with templates.</p>
</body>
</html>"""

if __name__ == '__main__':
    app.run(debug=True)
