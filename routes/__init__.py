from flask import Blueprint

# Create blueprints
upload_bp = Blueprint('upload', __name__)
health_bp = Blueprint('health', __name__)

# Import routes
from .upload import *
from .health import *

# List of all blueprints
blueprints = [upload_bp, health_bp]