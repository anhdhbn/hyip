# coding=utf-8
import logging

from sqlalchemy import or_

from hyip import models

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


def save_user_to_database(**kwargs):
    user = models.User(**kwargs)
    models.db.session.add(user)
    models.db.session.commit()
    return user


def find_one_by_email(email):
    user = models.User.query.filter(
        models.User.email == email
    ).first()

    return user or None


def find_one_by_username(username):
    user = models.User.query.filter(
        models.User.username == username
    ).first()

    return user or None


def delete_one_by_email(email):
    models.User.query.filter(
        models.User.email == email
    ).delete()
    models.db.session.commit()


def find_one_by_email_or_username_ignore_case(email, username):
    user = models.User.query.filter(
        or_(
            models.User.username == username,
            models.User.email == email
        )
    ).first()  # type: m.User

    return user or None
