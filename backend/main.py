# coding=utf-8
import logging
import os

from dotenv import load_dotenv

from hyip import app

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)

_DOT_ENV_PATH = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(_DOT_ENV_PATH)

from hyip.models import db, User

@app.cli.command("dropdb")
def drop():
    db.drop_all()

@app.cli.command("initdb")
@app.cli.command("resetdb")
def resetdb():
    db.drop_all()
    db.create_all()

@app.cli.command("createsuperuser")
def create_super_user():
    username = input("Vui long nhap user\n")
    email = input("Vui long nhap email\n")
    fullname  = input("Vui long nhap ten\n")
    password = input("Vui long nhap password\n")
    is_admin = True
    user = User(username=username, email=email, fullname=fullname, password=password, is_admin=is_admin)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)