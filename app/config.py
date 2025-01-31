from dotenv import load_dotenv
import os

load_dotenv()

POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")

MODE = os.environ.get("MODE")

LIFETIME_SECONDS = int(os.environ.get("LIFETIME_SECONDS"))
RESET_PASSWORD_TOKEN_SECRET = os.environ.get("RESET_PASSWORD_TOKEN_SECRET")
VERIFICATION_TOKEN_SECRET = os.environ.get("VERIFICATION_TOKEN_SECRET")

MONGO_URL = os.environ.get("MONGO_URL")
