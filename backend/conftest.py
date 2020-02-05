
# coding=utf-8
import logging

import pytest

__author__ = 'AnhDH'
_logger = logging.getLogger(__name__)


@pytest.fixture(autouse=True)
def app(request):
    from hyip import app
    from hyip.models import db

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    # test db initializations go below here
    db.create_all()

    def teardown():
        db.session.remove()
        db.drop_all()
        ctx.pop()

    request.addfinalizer(teardown)
    return app