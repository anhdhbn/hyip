from celeryapp import celery
import pytest

@pytest.fixture(scope='module')
def celery_app(request):
    celery.conf.update(CELERY_ALWAYS_EAGER=True)
    return celery