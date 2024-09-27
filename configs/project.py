from os import environ

from dotenv import dotenv_values

env = dotenv_values(".env")

# HOST = environ.get("HOST", env["HOST"])
# PORT = environ.get("PORT", env["PORT"])
ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS", env["ALLOWED_HOSTS"])
DEBUG = environ.get("DEBUG", env["DEBUG"])
SECRET_KEY = environ.get("SECRET_KEY", env["SECRET_KEY"])
