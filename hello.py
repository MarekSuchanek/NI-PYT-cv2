from datetime import datetime
import jinja2
import os

from flask import Flask, Blueprint, url_for, render_template, current_app

bp = Blueprint('bp', __name__, url_prefix='/example')


@bp.route('/')
def index():
    current_app.logger.debug('Někdo šel na index')
    link = url_for('bp.hello', name='Miro')
    answer = current_app.config['secret']
    return f'<html><head><body><a href="{link}" style="font-size: 20px;">Pozdravit Mira</a><br>Btw answer is {answer}'


@bp.route('/xhello/')
@bp.route('/xhello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@bp.route('/date')
def date_example():
    return render_template('date_example.html', created_at='Tue Mar 21 15:50:59 +0000 2017')


@bp.route('/secret')
def secret():
    return 'Secrets are secret!!!'


@bp.app_template_filter('time')
def convert_time(text):
    dt = datetime.strptime(text, '%a %b %d %H:%M:%S %z %Y')
    new_date = dt.strftime('%c')
    return jinja2.Markup(f'<span style="color:green;">') + new_date + jinja2.Markup('</span>')


def create_app(config=None):
    app = Flask(__name__)
    app.config['secret'] = 42
    app.register_blueprint(bp, url_prefix='/example2')
    return app


def main():
    print("hello")


print(f'Name is: {__name__}')


if __name__ == '__main__':
    main()
