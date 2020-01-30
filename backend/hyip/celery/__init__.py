from celery import Celery
cele = Celery("hyip")
cele.config_from_object("hyip.celery.settings")