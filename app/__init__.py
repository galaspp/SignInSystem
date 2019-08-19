from flask import Flask
from config import Config

UPLOAD_FOLDER = 'Manufacturing'

app = Flask(__name__)
app.config.from_object(Config)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
app.config['SERVER_NAME'] = 'rosegpe:8000'

from app import routes