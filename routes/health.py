from flask import jsonify
from __init__ import health_bp

@health_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200