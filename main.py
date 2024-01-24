from flask import Flask, render_template, request, url_for

#create a secret key for security
import os

import utils as util
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key')

@app.route('/')
def index():
  title = "Home"
  return render_template("index.html",title=title)


@app.route('/about')
def about():
  title = "About"
  return render_template("about.html",title=title)


app.run(host='0.0.0.0', port=81)


