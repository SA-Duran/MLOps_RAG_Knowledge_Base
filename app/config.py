import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    AWS_REGION = os.getenv("AWS_REGION")
    AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
    VECTOR_DB_PATH = 'vector_db'