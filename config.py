import os


class Config(object):
    SECRET_KEY = os.environ.get('secret-key') or 'some-secret-key'