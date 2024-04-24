from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

class Config:
    # Set the secret key to the value of the SECRET_KEY environment variables
    SQLALCHEMY_SECRET_KEY = os.getenv('SQLALCHEMY_SECRET_KEY')
    # print(SQLALCHEMY_SECRET_KEY)
    # Set the SQLALCHEMY_DATABASE_URI to the value of the DATABASE_URL environment variable
    # and the SQLALCHEMY_TRACK_MODIFICATIONS to the value of the SQLALCHEMY_TRACK_MODIFICATIONS environment variable
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')