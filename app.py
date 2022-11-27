from flask import Flask, render_template, request
import db
import secrets

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        db.add_comment(request.form['comment'])

    search_query = request.args.get('q')

    comments = db.get_comments(search_query)

    token = secrets.token_hex(20)

    return render_template('index.html',
                           comments=comments,
                           search_query=search_query, token=token)