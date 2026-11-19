from flask import Flask, redirect,render_template_string,request,url_for

app=Flask(__name__)

@app.route("/")
def home():
    return "<h1> Welcome</h1><p>Try /hello/Aisha, /add//12/30, /search?q=python, /greet</p>"

@app.route("/hello/<name>")
def hello(name):
    return render_template_string("<h1> Hello, {{ name }}! </h1>",name=name)

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return f"<h1>{a} + {b} ={a+b}</h1>"


@app.route("/search")
def search():
    q = request.args.get("q", "").strip()
    n = request.args.get("n", default=3, type=int)
    n = max(1, min(n, 20))
    if not q:
        return "Give me a search term, like /search?q=python", 400
    page = """
    <h1>Results for {{ q }}</h1>
    <ul>
      {% for i in range(1, n + 1) %}
        <li>{{ q }} result #{{ i }}</li>
      {% endfor %}
    </ul>
    """
    return render_template_string(page, q=q, n=n)


@app.errorhandler(404)
def not_found(error):
    return "<h1>404</h1><p>that page does not exist.</p>",404

if __name__ == "__main__":
    print("Flask application is starting...")
    app.run(debug=True)