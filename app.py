import project
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    url, title, artist, date, info = project.main()
    return render_template('index.html', url=url, title=title, artist=artist, date=date, info=info)


if __name__ == "__main__":
    app.run(debug=True)
