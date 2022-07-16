import project
from flask import Flask, render_template

app = Flask(__name__, template_folder='') # tells flask to look for HTML at the root directory


@app.route('/', methods=['POST', 'GET'])
def home():
    url, title, artist, date, info = project.main()
    return render_template('index.html', url=url, title=title, artist=artist, date=date, info=info)


if __name__ == "__main__":
    app.run(debug=True)
