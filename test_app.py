```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Test Flask Application is Working!"

@app.route("/test")
def test():
    return "Test successful!"

if __name__ == "__main__":
    app.run(debug=True, port=5001)
```
