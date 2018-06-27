# from flask import Flask
# from celery import Celery
#
#
# app = Flask(__name__)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
#
#
# celery = Celery(app.name, brocker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)