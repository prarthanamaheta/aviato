import os
from google.cloud import firestore
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

def get_firestore_client():
    """Initialize Firestore client"""
    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    if not credentials_path:
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS is not set or points to an invalid file.")

    if not os.path.exists(credentials_path):
        raise FileNotFoundError(f"The credentials file does not exist at {credentials_path}.")

    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
    return firestore.Client()

db = get_firestore_client()
