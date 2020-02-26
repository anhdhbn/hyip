# coding=utf-8
import logging
import os

from hyip import app

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


from hyip.models import db

@app.cli.command("dropdb")
def drop():
    db.drop_all()

@app.cli.command("initdb")
@app.cli.command("resetdb")
def resetdb():
    db.drop_all()
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)