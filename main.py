from flask import Flask, render_template, redirect
from datetime import datetime
from forms.user import RegisterForm
from data.jobs import Jobs
from data.news import News
from data.users import User
from data import db_session
import argparse
import sys

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


def main():
    db_session.global_init('db/blogs.db')
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs)
    return render_template("index.html", news=news)


@app.route('/1')
def sta():
    return render_template('base.html')


if __name__ == '__main__':
    main()
