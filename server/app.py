#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
