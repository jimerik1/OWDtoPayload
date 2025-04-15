from flask import Blueprint

# Create blueprints
upload_bp = Blueprint('upload', __name__)
health_bp = Blueprint('health', __name__)

# List of all blueprints
blueprints = [upload_bp, health_bp]

# Import routes AFTER creating blueprints
from . import upload, health