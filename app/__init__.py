from flask import Flask
from config import Config

UPLOAD_FOLDER = 'Manufacturing'

app = Flask(__name__)
app.config.from_object(Config)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024
app.run(host='0.0.0.0', port=8000, debug=True)

from app import routes