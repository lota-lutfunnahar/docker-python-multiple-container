import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"
    REDIS_DEV_URL = os.getenv("REDIS_URL", "redis://")
    
    #  "redis://:{passw}@{host}:{port}/0".format(passw=REDIS_PASS, host=REDIS_HOST, port=REDIS_PORT)

