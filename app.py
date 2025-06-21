from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('templates/*.html')  # следить за всеми HTML в templates/
    server.serve(debug=True, port=5000)  # можно указать порт
